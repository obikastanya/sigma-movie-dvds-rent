class HistoryRent {
  render() {
    let parameter = { userId: document.getElementById("hiddenUserId").value };
    fetch("/api/movie/rent/history", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        let content = [];
        if (!response.data.length) {
          return;
        }
        for (let [index, record] of response.data.entries()) {
          let template = `
          <tr>
          <td>${index + 1}</td>
          <td>${record.start_date}</td>
          <td>${record.due_date}</td>
          <td>${record.title}</td>
          </tr>`;
          content.push(template);
        }

        document.getElementById("history_table").innerHTML = content.join("");
      });
  }
}

class PaymentValidate {
  constructor() {
    this.find = this.find.bind(this);
    this.validatePayment = this.validatePayment.bind(this);
  }
  find(event) {
    document.getElementById("validateForm").innerHTML = "";
    let parameter = {
      invoiceId: document.getElementById("invoiceIdField").value,
    };
    if (!parameter.invoiceId) {
      alert("Invoice Id is empty");
      return;
    }
    fetch("/api/rent/invoice", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.data.length) {
          this.showFormPaymentValidate(response.data[0]);
        }
      });
  }
  validatePayment(event) {
    let parameter = {
      paymentImagePath: "",
      transactionDate: document.getElementById("transactionDateField").value,
      invoiceId: document.getElementById("invoiceIdField").value,
    };
    if (!parameter.transactionDate) {
      alert("Transaction date cant be empty");
      return;
    }
    const selectedFile = document.getElementById("paymentReceiptField")
      .files[0];
    if (!selectedFile) {
      alert("No image found");
      return;
    }
    this.uploadFile(selectedFile).then((response) => {
      if (response.status) {
        parameter.paymentImagePath = response.data[0].filename;
        fetch("/api/invoice/validate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(parameter),
        })
          .then((response) => response.json())
          .then((response) => {
            new HistoryRent().render();
            alert(response.message);
          });
      }
      alert(response.message);
    });
  }

  async uploadFile(file) {
    let formData = new FormData();
    formData.append("file", file);
    return await fetch("/api/invoice/upload", {
      method: "POST",
      body: formData,
    }).then((response) => response.json());
  }

  showFormPaymentValidate(invoice) {
    let form = `
    <form>

    <div class="mb-3" hidden>
      <input type="number" class="form-control" id="transactionIdField" value=${invoice.transaction_id}  hidden>
    </div>

    <div class="mb-3">
      <label for="invoiceIdField" class="form-label" >Invoice Number</label>
      <input type="number" class="form-control" id="invoiceIdField" value=${invoice.id}  disabled>
    </div>

    <div class="mb-3">
      <label for="nominalField" class="form-label" >Nominal</label>
      <input type="number" class="form-control" id="nominalField" value=${invoice.nominal}  disabled>
    </div>
    <div class="mb-3">
    <label for="transactionDateField" class="form-label" >Payment Date</label>
    <input type="date" class="form-control" id="transactionDateField" >
  </div>
    <div class="form-group">
      <label for="paymentReceiptField" class="form-label d-block" >Payment Receipt</label>
      <input type="file" class="form-control-file" id="paymentReceiptField">
      <div id="updateImgPreview"></div>
    </div>
    <button type="button" class="btn btn-primary mt-4" id="submitButtonId" onClick="new PaymentValidate().validatePayment(event)">Submit</button>
  </form>
`;
    document.getElementById("validateForm").innerHTML = form;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new HistoryRent().render();
  document
    .getElementById("buttonFindInvoices")
    .addEventListener("click", new PaymentValidate().find);
});
