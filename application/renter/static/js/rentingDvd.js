class RentingDvd {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let id = document.getElementById("hiddenMovieId").value;
    fetch(`/api/review/movie/${id}`)
      .then((response) => response.json())
      .then((response) => {
        this.setMovieDetail(response.movieData);
      });
  }
  setMovieDetail(movie) {
    if (movie.image_path && movie.image_path.length > 5) {
      document.getElementById("posterId").innerHTML = `
      <img src="/${movie.image_path}" width='350' alt="">`;
    }
    console.log(movie);
    let setValue = (id, value) =>
      (document.getElementById(id).innerText = value);
    setValue("title", movie.title);
    setValue("genre", movie.genre);
    setValue("releaseDate", movie.release_date);
    setValue("ageCertification", movie.age_certification);
    setValue("availableStock", movie.available_stock);
    setValue("desc", movie.desc);
    setValue("price", movie.price);
  }
}
class RentingSubmit {
  constructor() {
    this.submit = this.submit.bind(this);
  }
  submit() {
    let parameter = {
      movieId: document.getElementById("movieIdField").value,
      userId: document.getElementById("userIdField").value,
      startDate: document.getElementById("startDateField").value,
      endDate: document.getElementById("endDateField").value,
      address: document.getElementById("addressField").value,
    };
    fetch("/api/movie/rent", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        alert(response.message);
        if (response.status) {
          this.showInvoices(response.data[0]);
        }
      });
  }
  showInvoices(invoices) {
    let invoicesTemplate = `
          <p>Invoices Number : ${invoices.invoicesId}</p>
          <p>Payment Nominal : ${invoices.nominal}</p>
          <p>Bank Account  : ${invoices.bank}</p>
          <p>Pay before ${invoices.payment_due}</p>
          <p>*Keep your invoices id, you gonna need it for payment validation.</p>
          <p><a href="/history">Validate your payment here.</a> </p>
        `;
    document.getElementById("invoicesNote").innerHTML = invoicesTemplate;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new RentingDvd().render();
  document
    .getElementById("submitButtonId")
    .addEventListener("click", new RentingSubmit().submit);
});
