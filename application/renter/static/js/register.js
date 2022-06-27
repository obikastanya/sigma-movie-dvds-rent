class Register {
  constructor() {
    this.submit = this.submit.bind(this);
  }
  submit(event) {
    let parameter = this.getRegistrationData();
    if (!this.cantBeEmpty(parameter)) {
      alert("Please complete the form");
      return;
    }
    console.log(parameter.password);

    if (parameter.password !== parameter.confirmPassword) {
      alert("Password unmatch");
      return;
    }
    fetch("/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    });
  }
  getRegistrationData() {
    let gender = "";
    try {
      gender = document.querySelector(
        'input[name="genderField"]:checked'
      ).value;
    } catch {}
    let getValue = (id) => document.getElementById(id).value;
    return {
      address: getValue("addressField"),
      birth_date: getValue("birthDateField"),
      email: getValue("emailField"),
      gender: gender,
      name: getValue("nameField"),
      name: getValue("addressField"),
      password: getValue("passwordField"),
      confirmPassword: getValue("passwordConfirmField"),
    };
  }
  cantBeEmpty(parameter) {
    for (let [key, value] of Object.entries(parameter)) {
      if (!value) return false;
    }
    return true;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("registerButtonId")
    .addEventListener("click", new Register().submit);
});
