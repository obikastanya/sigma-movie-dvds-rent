class Notif {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let parameter = { userId: document.getElementById("hiddenUserId").value };

    fetch("/alert", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        this.showNotif(response.data[0].alerts);
      });
  }
  showNotif(data) {
    let notifContainer = document.getElementById("alertContainerId");
    for (let notif of data) {
      let template = `
      <div class="card my-3" >
          <div class="card-body">
            <h5 class="card-title">${notif.title}</h5>
            <p class="card-text">${notif.desc}</p>
            </div>
        </div>
    `;

      notifContainer.innerHTML += template;
    }
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new Notif().render();
});
