class TableAction {
  constructor() {
    this.editData = this.editData.bind(this);
    this.deleteData = this.deleteData.bind(this);
    this.addData = this.addData.bind(this);
  }
  editData(event) {
    let id = event.target.getAttribute("data-id");
    fetch("/admin/api/index/" + id)
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
    fetch("/admin/api/index", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: id }),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.status) {
          $("#admin_datatable_id").DataTable().ajax.reload();
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
    this.saveAdminData = this.saveAdminData.bind(this);
  }
  saveData() {
    let getValue = (id) => document.getElementById(id).value;
    let parameter = {
      active_status: "Y",
      name: getValue("nameField"),
      password: getValue("passwordField"),
      email: getValue("emailField"),
    };
    if (!(parameter.password && parameter.name && parameter.email)) {
      alert("Please complete the form");
      return;
    }
    return this.saveAdminData(parameter);
  }
  setEmptyForm() {
    let setValue = (id) => (document.getElementById(id).value = "");
    setValue("nameField");
    setValue("passwordField");
    setValue("emailField");
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
    if (!(parameter.name && parameter.email)) {
      alert("Please complete the form");
      return;
    }
    return this.updateAdminData(parameter);
  }
  saveAdminData(parameter) {
    fetch("/admin/api/index", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        $("#admin_datatable_id").DataTable().ajax.reload();
        alert(response.message);
        if (response.status) {
          this.setEmptyForm();
        }
      });
  }
  updateAdminData(parameter) {
    fetch("/admin/api/index", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        $("#admin_datatable_id").DataTable().ajax.reload();
        alert(response.message);
        if (response.status) {
          document.getElementById("modal_edit_close_button").click();
        }
      });
  }
}

class DatatabaleComponent {
  render() {
    const datatable = $("#admin_datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/api/index",
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
          data.email = getDataFromFields("#adminEmail");
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
      $("#admin_datatable_id").DataTable().ajax.reload();
    });
  }
}

$(document).ready(function () {
  new DatatabaleComponent().render();
  new FormFilter().registerEvent();
  new TableAction().registerEvent();
});
