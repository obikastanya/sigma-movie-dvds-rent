class TableAction {
  constructor() {
    this.editData = this.editData.bind(this);
    this.deleteData = this.deleteData.bind(this);
    this.addData = this.addData.bind(this);
  }
  editData(event) {}
  deleteData(event) {
    console.log(event);
  }
  addData(event) {
    this.showModal("#id_modal_for_add_new_data");
  }
  showModal(idModal) {
    $(idModal).modal("show");
  }
}

class DatatabaleMovie {
  render() {
    const datatable = $("#movie_dvd_datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/dvd",
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
          data.id = getDataFromFields("#movieId");
          data.title = getDataFromFields("#movieTitle");
        },
      },
      columns: [
        {
          data: null,
          defaultContent: "",
        },
        { data: "id" },
        { data: "title" },
        { data: "desc" },
        { data: "genre" },
        { data: "release_date" },
        { data: "total_dvds" },
        { data: "available_stock" },
        {
          data: null,
          render: (data) => {
            let buttonEdit = `<button type="button" class="btn btn-warning btn-edit-data" onClick='new TableAction().editData(event)' >Edit</button>`;
            let buttonDelete = `<button type="button" class="btn btn-danger btn-delete-data" onClick='new TableAction().deleteData(event)'>Delete</button>`;
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
});
