class Profile {
  constructor() {
    this.render = this.render.bind(this);
  }
  render(event) {
    let parameter = { userId: document.getElementById("hiddenUserId").value };

    fetch("/api/user/index", {
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
        setValue("oldPasswordField", "");
        setValue("newpasswordField", "");
        setValue("newPasswordConfirmField", "");
        document.getElementById("addressField").innerText = user.address;
        if (user.gender == "L") {
          document.getElementById("maleField").checked = true;
        } else {
          document.getElementById("femaleField").checked = true;
        }
      });
  }
  update() {
    let gender = "";
    try {
      gender = document.querySelector(
        'input[name="genderField"]:checked'
      ).value;
    } catch {}
    let getValue = (id) => document.getElementById(id).value;
    let parameter = {
      userId: getValue("hiddenUserId"),
      address: getValue("addressField"),
      birth_date: getValue("birthDateField"),
      email: getValue("emailField"),
      gender: gender,
      name: getValue("nameField"),
      password: getValue("oldPasswordField"),
      newPassword: getValue("newpasswordField"),
      newPasswordConfirm: getValue("newPasswordConfirmField"),
    };

    for (let [key, value] of Object.entries(parameter)) {
      if (
        ["userId", "password", "newPassword", "newPasswordConfirm"].includes(
          key
        )
      )
        continue;
      if ([null, undefined, ""].includes(value)) {
        alert("Please Complete the form");
        return;
      }
    }

    if (!parameter.password) {
      alert("Password is required to make a change");
      return;
    }
    if (parameter.newPassword !== parameter.newPasswordConfirm) {
      alert("New Password unmatch");
      return;
    }
    fetch("/api/user/index", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        alert(response.message);
        new Profile().render();
      });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new Profile().render();
  document
    .getElementById("updateButtonId")
    .addEventListener("click", new Profile().update);
});
