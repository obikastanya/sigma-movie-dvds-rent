$(document).ready(function () {
  const datatable = $("#movie_dvd_datatable_id").DataTable({
    processing: true,
    serverSide: true,
    ajax: {
      url: "/admin/dvd",
      method: "GET",
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
          let buttonEdit = `<button type="button" class="btn btn-warning btn-edit-data" 
                    value="_data_">Edit</button>`;
          let buttonDelete = `<button type="button" class="btn btn-danger btn-delete-data"
                    >Delete</button>`;
          return buttonEdit + "&nbsp;" + buttonDelete;
        },
      },
    ],
    dom: `<'toolbar col col-sm-12 col-md-12 col-lg-6 justfiy-content-left text-left'>`,
    fnInitComplete: () => {
      //Set button create new data for toolbar
      $("div.toolbar").html(`<button type="button" class="btn btn-success" 
        >Add New Data</button>`);
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
});

