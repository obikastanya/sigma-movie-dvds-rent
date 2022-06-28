class ReviewDvd {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let id = document.getElementById("hiddenMovieId").value;
    fetch(`/api/review/movie/${id}`)
      .then((response) => response.json())
      .then((response) => {
        console.log(response);
        let reviews = this.createReview(response.data);
        if (!reviews.length) {
          document.getElementById("reviewContainerId").innerHTML =
            "<p>No reviews yet.</p>";
        } else {
          document.getElementById("reviewContainerId").innerHTML =
            reviews.join("");
        }
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
  createReview(data) {
    let reviews = [];
    for (let review of data) {
      let template = `
            <div className="row mx-2 mb-1 ">
            <p className="mb-0">
              <span className="h6"> ${review.users.name}</span>
              <small className="ms-2 text-secondary">(Rate: ${review.rate}) </small>
            </p>
            <p>
              <small>${review.desc}</small>
            </p>
          </div>`;
      reviews.push(template);
    }
    return reviews;
  }
}
class ReviewSubmit {
  constructor() {
    this.submit = this.submit.bind(this);
  }
  submit() {
    let parameter = {
      movieId: document.getElementById("hiddenMovieId").value,
      desc: document.getElementById("reviewField").value,
      rate: document.querySelector('input[name="rate"]:checked').value,
    };
    fetch("/api/review/movie", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.status) {
          new ReviewDvd().render();
        }

        alert(response.message);
      });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new ReviewDvd().render();
  document
    .getElementById("submitButtonId")
    .addEventListener("click", new ReviewSubmit().submit);
});
