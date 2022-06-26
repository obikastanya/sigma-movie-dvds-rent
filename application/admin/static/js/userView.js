class TableAction {
  constructor() {
    this.banUser = this.banUser.bind(this);
    this.deleteData = this.deleteData.bind(this);
  }
  banUser(event) {
    let id = event.target.getAttribute("data-id");
    fetch("/admin/user/" + id)
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

  showModal(idModal) {
    $(idModal).modal("show");
  }
  registerEvent() {
    document
      .getElementById("button_save_updated_data_id")
      .addEventListener("click", new ApiAction().updateData);
  }
}

class ApiAction {
  constructor() {
    this.updateData = this.updateData.bind(this);
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
        url: "/admin/users",
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
          data.id = getDataFromFields("#userEmail");
          data.name = getDataFromFields("#userName");
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
        { data: "gender" },
        { data: "birth_date" },
        { data: "address" },
        {
          data: null,
          render: (data) => {
            if (data.banned_status == "B") {
              return `<button type="button" class="btn btn-success btn-edit-data" data-id=${data.id} onClick='new TableAction().banUser(event)' >Release</button>`;
            }
            return `<button type="button" class="btn btn-danger btn-delete-data" data-id=${data.id} onClick='new TableAction().deleteData(event)'>Ban</button>`;
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
      $("#datatable_id").DataTable().ajax.reload();
    });
  }
}

$(document).ready(function () {
  new DatatabaleComponent().render();
  new FormFilter().registerEvent();
  new TableAction().registerEvent();
});
