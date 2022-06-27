class TableAction {
  constructor() {
    this.editData = this.editData.bind(this);
    this.deleteData = this.deleteData.bind(this);
    this.addData = this.addData.bind(this);
  }
  editData(event) {
    let id = event.target.getAttribute("data-id");
    fetch("/admin/index/" + id)
      .then((response) => response.json())
      .then((response) => {
        let admin = response.data[0];
        let setValue = (id, value) => {
          let element = document.getElementById(id);
          element.value = value;
        };
        setValue("idFieldUpd", admin.id);
        setValue("nameFieldUpd", admin.name);
        setValue("emailFieldUpd", admin.email);
        $("#id_modal_for_edit").modal("show");
      });
  }

  deleteData(event) {
    let id = event.target.getAttribute("data-id");
    fetch("/admin/index", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: id }),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.status) {
          $("#datatable_id").DataTable().ajax.reload();
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
      name: getValue("nameField"),
      password: getValue("passwordField"),
      email: getValue("emailField"),
    };
    return this.saveAdminData(parameter);
  }
  updateData() {
    let getValue = (id) => document.getElementById(id).value;
    let parameter = {
      active_status: "Y",
      name: getValue("nameFieldUpd"),
      password: getValue("passwordFieldUpd"),
      email: getValue("emailFieldUpd"),
      id: getValue("idFieldUpd"),
    };
    return this.updateAdminData(parameter);
  }
  saveAdminData(parameter) {
    fetch("/admin/index", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        $("#datatable_id").DataTable().ajax.reload();
        alert(response.message);
      });
  }
  updateAdminData(parameter) {
    fetch("/admin/index", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        $("#datatable_id").DataTable().ajax.reload();
        alert(response.message);
      });
  }
}

class DatatabaleComponent {
  render() {
    const datatable = $("#datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/dvd-renter/data",
        method: "GET",
      },
      columns: [
        {
          data: null,
          defaultContent: "",
        },
        { data: "name" },
        { data: "rent_start_date" },
        { data: "rent_due_date" },
        {
          data: "movie",
          render: (data) => {
            if (data) {
              let titles = [];
              for (let movie of data) {
                titles.push(movie[1]);
              }
              return titles;
            }
            return "-";
          },
        },
        {
          data: null,
          render: (data) => {
            let buttonDelete = `<button type="button" class="btn btn-danger btn-delete-data" data-id=${
              data.id
            } data=${JSON.stringify(
              data
            )} onClick='new TableAction().deleteData(event)'>Alert</button>`;
            return buttonDelete;
          },
        },
      ],
      dom: `<'toolbar col col-sm-12 col-md-12 col-lg-6 justfiy-content-left text-left'>`,
      fnInitComplete: () => {},
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
      $("#datatable_id").DataTable().ajax.reload();
    });
  }
}

$(document).ready(function () {
  new DatatabaleComponent().render();
});
