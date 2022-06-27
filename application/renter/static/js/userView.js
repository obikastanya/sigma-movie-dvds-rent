class TableAction {
  constructor() {
    this.banUser = this.banUser.bind(this);
    this.releaseUser = this.releaseUser.bind(this);
  }
  banUser(event) {
    let id = event.target.getAttribute("data-id");
    document.getElementById("idField").value = id;
    $("#id_modal_for_edit").modal("show");
  }

  releaseUser(event) {
    let id = event.target.getAttribute("data-id");
    document.getElementById("idField").value = id;
    let parameter = {
      id: id,
    };
    fetch("/admin/users/release", {
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

  showModal(idModal) {
    $(idModal).modal("show");
  }
  registerEvent() {
    document
      .getElementById("button_save_updated_data_id")
      .addEventListener("click", new ApiAction().applyBanUser);
  }
}

class ApiAction {
  constructor() {
    this.applyBanUser = this.applyBanUser.bind(this);
  }
  applyBanUser() {
    let getValue = (id) => document.getElementById(id).value;
    let parameter = {
      id: getValue("idField"),
      desc: getValue("descField"),
    };
    fetch("/admin/users/ban", {
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
              return `<button type="button" class="btn btn-success btn-delete-data" data-id=${data.id} onClick='new TableAction().releaseUser(event)' >Release</button>`;
            }
            return `<button type="button" class="btn btn-danger btn-bann-user" data-id=${data.id} onClick='new TableAction().banUser(event)'>Ban</button>`;
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
  new FormFilter().registerEvent();
  new TableAction().registerEvent();
});
