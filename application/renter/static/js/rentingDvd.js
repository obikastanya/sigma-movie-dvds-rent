class RentingDvd {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let id = document.getElementById("hiddenMovieId").value;
    fetch(`/user/review/dvd-data/${id}`)
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
  }
}
class RentingSubmit {
  constructor() {
    this.submit = this.submit.bind(this);
  }
  submit() {
    let parameter = {
      movieId: document.getElementById("hiddenMovieId").value,
      desc: document.getElementById("reviewField").value,
      rate: document.querySelector('input[name="rate"]:checked').value,
    };
    fetch("/user/review/dvd-data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.status) {
          new RentingDvd().render();
        }

        alert(response.message);
      });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new RentingDvd().render();
  document
    .getElementById("submitButtonId")
    .addEventListener("click", new ReviewSubmit().submit);
});
