class NotifNumber {
  render() {
    let parameter = {
      userId: document.getElementById("notifUserId").value,
    };
    fetch("/api/alert/count", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response.data.length) {
          let countedData = response.data[0];
          document.getElementById("notifId").innerText = countedData.total;
        }
      });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  new NotifNumber().render();
});
