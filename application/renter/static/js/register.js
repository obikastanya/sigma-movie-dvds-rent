class Register {
  submit() {}
}

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("registerButtonId")
    .addEventListener("click", function (id) {
      console.log("submit");
    });
});
