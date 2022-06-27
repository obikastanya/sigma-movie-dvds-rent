class Profile {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let parameter = { userId: document.getElementById("hiddenUserId").value };
    console.log(parameter);

    fetch("/user/index", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        let user = response.data[0];
        let setValue = (id, value) =>
          (document.getElementById(id).value = value);

        setValue("birthDateField", user.birth_date);
        setValue("emailField", user.email);

        setValue("nameField", user.name);
        document.getElementById("addressField").innerText = user.address;
        if (user.gender == "L") {
          document.getElementById("maleField").checked = true;
        } else {
          document.getElementById("femaleField").checked = true;
        }
      });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new Profile().render();
});
