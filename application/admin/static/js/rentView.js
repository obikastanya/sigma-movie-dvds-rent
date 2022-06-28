class TableAction {
  constructor() {
    this.alertUser = this.alertUser.bind(this);
  }

  alertUser(event) {
    let id = event.target.getAttribute("data-user-id");
    let movie = event.target.getAttribute("data-movie");
    let dueDate = event.target.getAttribute("");
    let message = `
    The deadline for borrowing the dvd (${movie}) has expired on ${dueDate}. Please return the book as soon as possible.
    `;
    fetch("/admin/api/renter/alert", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userId: id, message: message }),
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
    const datatable = $("#datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/api/renter",
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
            let titles = [];
            for (let movie of data.movie) {
              titles.push(movie[1]);
            }

            let disabled = "";
            if (data.due_status == "N") {
              disabled = "disabled";
            }
            let buttonDelete = `<button type="button" class="btn btn-danger btn-delete-data" data-user-id=${
              data.user_id
            } data-due-date=${data.rent_due_date} data-movie=${titles.join(
              ","
            )} onClick='new TableAction().alertUser(event)' ${disabled}>Alert</button>`;
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
