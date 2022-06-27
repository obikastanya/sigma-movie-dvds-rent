class TableAction {
  constructor() {
    this.validatePayment = this.validatePayment.bind(this);
  }
  showPaymentReceipt(event) {
    let direction = event.target.getAttribute("data-payment-image");
    let a = document.createElement("a");
    a.target = "_blank";
    a.href = "/" + direction;
    a.click();
  }

  validatePayment(event) {
    let id = event.target.getAttribute("data-id");
    console.log(id);
    fetch("/admin/invoices/data/validate", {
      method: "POST",
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
}

class DatatabaleComponent {
  render() {
    const datatable = $("#datatable_id").DataTable({
      processing: true,
      serverSide: true,
      ajax: {
        url: "/admin/invoices/data",
        method: "GET",
      },
      columns: [
        {
          data: null,
          defaultContent: "",
        },
        { data: "id" },
        { data: "transaction_id" },
        {
          data: null,
          render: (data) => {
            return data.transaction.user.name;
          },
        },
        { data: "nominal" },
        { data: "transaction_date" },
        { data: "validation_date" },
        {
          data: null,
          render: (data) => {
            let disabled = "";
            if (data.validation_date) {
              disabled = "disabled";
            }
            let paymentReceipt = `<button type="button" class="btn btn-secondary btn-delete-data" data-payment-image=${data.payment_receipt} onClick='new TableAction().showPaymentReceipt(event)' >Payment Receipt</button>`;
            let buttonValidate = `<button type="button" class="btn btn-primary btn-delete-data" data-id=${data.id} onClick='new TableAction().validatePayment(event)' ${disabled}>Validate</button>`;
            return buttonValidate + "&nbsp;" + paymentReceipt;
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
