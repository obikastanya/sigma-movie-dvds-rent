class TableAction {
  constructor() {
    this.deleteData = this.deleteData.bind(this);
  }
  deleteData(event) {
    let userId = event.target.getAttribute("data-user-id");
    let movieId = event.target.getAttribute("data-id");
    fetch("/admin/api/review", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ movieId: movieId, userId: userId }),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.status) {
          $("#datatable_id").DataTable().ajax.reload();
        }
        alert(response.message);
      });
  }
}

class DatatabaleComponent {
  render() {
    let id = document.getElementById("movieId").value;
    const datatable = $("#datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/api/review/" + id,
        method: "GET",
      },
      columns: [
        {
          data: null,
          defaultContent: "",
        },
        {
          data: null,
          render: (data) => {
            return data.users.name;
          },
        },
        { data: "desc" },
        { data: "rate" },
        {
          data: null,
          render: (data) => {
            let buttonDelete = `<button type="button" class="btn btn-danger btn-delete-data" data-id=${data.id} data-user-id=${data.users.id} onClick='new TableAction().deleteData(event)'>Delete</button>`;
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

$(document).ready(function () {
  new DatatabaleComponent().render();
});
