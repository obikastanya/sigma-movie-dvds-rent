class TableAction {
  constructor() {
    this.editData = this.editData.bind(this);
    this.deleteData = this.deleteData.bind(this);
    this.addData = this.addData.bind(this);
  }
  editData(event) {
    let idMovie = event.target.getAttribute("data-id");
    fetch("/admin/dvd/" + idMovie)
      .then((response) => response.json())
      .then((response) => {
        console.log(response);
        let movie = response.data[0];
        let setValue = (id, value) => {
          let element = document.getElementById(id);
          console.log(element);
          element.value = value;
        };
        setValue("idFieldUpd", movie.id);
        setValue("ageFieldUpd", movie.age_certification);
        setValue("totalDvdFieldUpd", movie.available_stock);
        setValue("descFieldUpd", movie.desc);
        setValue("genreFieldUpd", movie.genre);
        setValue("releaseDateFieldUpd", movie.release_date);
        setValue("titleFieldUpd", movie.title);
        setValue("totalDvdFieldUpd", movie.total_dvds);
        document.getElementById("updateImgPreview").innerHTML = `
        <img src='/${movie.image_path}' alt="Poster" width="200" />`;
        $("#id_modal_for_edit").modal("show");
      });
  }

  deleteData(event) {
    let idMovie = event.target.getAttribute("data-id");
    fetch("/admin/dvd", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: idMovie }),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.status) {
          $("#movie_dvd_datatable_id").DataTable().ajax.reload();
        }
        alert(response.message);
      });
  }
  addData(event) {
    this.showModal("#id_modal_for_add_new_data");
  }
  showModal(idModal) {
    $(idModal).modal("show");
  }
  registerEvent() {
    document
      .getElementById("new_data_save_button_id")
      .addEventListener("click", new ApiAction().saveData);
    document
      .getElementById("button_save_updated_data_id")
      .addEventListener("click", new ApiAction().updateData);
  }
}

class ApiAction {
  constructor() {
    this.saveData = this.saveData.bind(this);
    this.updateData = this.updateData.bind(this);
  }
  saveData() {
    let getValue = (id) => document.getElementById(id).value;
    let parameter = {
      active_status: "Y",
      age_certification: getValue("ageField"),
      available_stock: getValue("totalDvdField"),
      desc: getValue("descField"),
      genre: getValue("genreField"),
      image_path: "/",
      release_date: getValue("releaseDateField"),
      title: getValue("titleField"),
      total_dvds: getValue("totalDvdField"),
    };
    const selectedFile = document.getElementById("posterField").files[0];
    if (!selectedFile) {
      alert("No image found");
      return;
    }
    this.uploadFile(selectedFile).then((response) => {
      if (response.status) {
        parameter.image_path = response.data[0].filename;
        return this.saveDvdData(parameter);
      }
      alert(response.message);
    });
  }
  updateData() {
    let getValue = (id) => document.getElementById(id).value;
    let parameter = {
      active_status: "Y",
      id: getValue("idFieldUpd"),
      age_certification: getValue("ageFieldUpd"),
      available_stock: getValue("totalDvdFieldUpd"),
      desc: getValue("descFieldUpd"),
      genre: getValue("genreFieldUpd"),
      image_path: getValue("posterPathFieldUpd"),
      release_date: getValue("releaseDateFieldUpd"),
      title: getValue("titleFieldUpd"),
      total_dvds: getValue("totalDvdFieldUpd"),
    };
    const selectedFile = document.getElementById("posterField").files[0];
    if (selectedFile) {
      this.uploadUpdateFile(selectedFile).then((response) => {
        if (response.status) {
          parameter.image_path = response.data[0].filename;
          return this.updateDvdData(parameter);
        }
        alert(response.message);
      });

      return;
    } else {
      return this.updateDvdData(parameter);
    }
  }
  saveDvdData(parameter) {
    fetch("/admin/dvd", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        $("#movie_dvd_datatable_id").DataTable().ajax.reload();
        alert(response.message);
      });
  }
  async uploadFile(file) {
    let formData = new FormData();
    formData.append("file", file);
    return await fetch("/admin/dvd/upload", {
      method: "POST",
      body: formData,
    }).then((response) => response.json());
  }
  updateDvdData(parameter) {
    fetch("/admin/dvd", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        $("#movie_dvd_datatable_id").DataTable().ajax.reload();
        alert(response.message);
      });
  }
  async uploadUpdateFile(file) {
    let formData = new FormData();
    formData.append("file", file);
    return await fetch("/admin/dvd/upload", {
      method: "POST",
      body: formData,
    }).then((response) => response.json());
  }
}

class DatatabaleMovie {
  render() {
    const datatable = $("#movie_dvd_datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/index",
        method: "GET",
        data: (data) => {
          const getDataFromFields = (id) => {
            try {
              const value = document.querySelector(id).value;
              return value;
            } catch (e) {
              return null;
            }
          };
          data.id = getDataFromFields("#adminEmail");
          data.name = getDataFromFields("#adminName");
        },
      },
      columns: [
        {
          data: null,
          defaultContent: "",
        },
        { data: "id" },
        { data: "name" },
        { data: "email" },
        {
          data: null,
          render: (data) => {
            let buttonEdit = `<button type="button" class="btn btn-warning btn-edit-data" data-id=${data.id} onClick='new TableAction().editData(event)' >Edit</button>`;
            let buttonDelete = `<button type="button" class="btn btn-danger btn-delete-data" data-id=${data.id} onClick='new TableAction().deleteData(event)'>Delete</button>`;
            return buttonEdit + "&nbsp;" + buttonDelete;
          },
        },
      ],
      dom: `<'toolbar col col-sm-12 col-md-12 col-lg-6 justfiy-content-left text-left'>`,
      fnInitComplete: () => {
        $("div.toolbar").html(
          `<button type="button" class="btn btn-success" onClick='new TableAction().addData(event)'>Add New Data</button>`
        );
      },
    });
    datatable
      .on("draw.dt order.dt search.dt", function () {
        datatable
          .column(0, { search: "applied", order: "applied" })
          .nodes()
          .each(function (cell, i) {
            cell.innerHTML = i + 1;
          });
      })
      .draw();
  }
}

class FormFilter {
  registerEvent() {
    let buttonFilter = document.getElementById("filterButtonId");
    buttonFilter.addEventListener("click", function (event) {
      $("#movie_dvd_datatable_id").DataTable().ajax.reload();
    });
  }
}

$(document).ready(function () {
  new DatatabaleMovie().render();
  new FormFilter().registerEvent();
  new TableAction().registerEvent();
});
