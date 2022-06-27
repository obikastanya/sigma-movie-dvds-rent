class StoreDvd {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    fetch("/user/dvd")
      .then((response) => response.json())
      .then((response) => {
        if (response.data) {
          let movieContainer1 = [];
          let movieContainer2 = [];
          let movieContainer3 = [];
          let movieList = this.createCard(response.data);
          let position = 1;
          for (let movie of movieList) {
            if (position == 1) {
              movieContainer1.push(movie);
            } else if (position == 2) {
              movieContainer2.push(movie);
            } else {
              movieContainer3.push(movie);
            }
            if (position == 3) {
              position = 1;
            } else {
              position += 1;
            }
          }
          document.getElementById("movie_container1_id").innerHTML =
            movieContainer1.join("");

          document.getElementById("movie_container2_id").innerHTML =
            movieContainer2.join("");

          document.getElementById("movie_container3_id").innerHTML =
            movieContainer3.join("");
        } else {
          document.getElementById("movie_container_id").innerHTML =
            "<h5>No Movie Found <h5>";
        }
        if (!response.status) {
          alert(response.message);
        }
      });
  }

  createCard(movies) {
    let content = [];
    for (let movie of movies) {
      if (!movie.image_path || movie.image_path.length < 5) {
        movie.image_path = "/static/defaultImage/posterMovie.png";
      }
      let disabledRent = "";
      if (movie.available_stock < 1) {
        disabledRent = "disabled";
      }
      let template = `
          <div class="row card position-relative mx-3 py-1">
            <img src="/${movie.image_path}" class="card-img-top"  alt="Poster">
            <div class="card-body">
              <h5 class="card-title">${movie.title}</h5>
              <p class="card-text"> ${movie.genre}</p>
              <p class="card-text">${movie.desc}</p>
              <p class="card-text"> Available : ${movie.available_stock} dvds</p>
              <p class="card-text">Status : On Air</p>
              <a href="/dvd/rent/${movie.id}" class="btn btn-primary" ${disabledRent}>Rent</a>
              <a href=/review/dvd/${movie.id} class="btn btn-warning">Review</a>
            </div>
          </div>
      `;
      content.push(template);
    }
    return content;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new StoreDvd().render();
});
