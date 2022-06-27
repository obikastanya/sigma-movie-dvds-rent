class ReviewDvd {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let id = document.getElementById("hiddenMovieId").value;
    fetch(`/user/review/dvd-data/${id}`)
      .then((response) => response.json())
      .then((response) => {
        let reviews = this.createReview(response.data);
        if (!reviews) {
          document.getElementById("reviewContainerId").innerHTML =
            "<p>No reviews yet.</p>";
          return;
        }
        this.setMovieDetail(response.movieData);
        document.getElementById("reviewContainerId").innerHTML =
          reviews.join("");
      });
  }
  setMovieDetail(movie) {
    if (movie.image_path && movie.image_path.length > 5) {
      document.getElementById("posterId").innerHTML = `
      <img src="${movie.image_path}" alt="">`;
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

document.addEventListener("DOMContentLoaded", function () {
  new ReviewDvd().render();
});
