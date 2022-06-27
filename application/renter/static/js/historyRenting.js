class HistoryRent {
  render() {
    let parameter = { userId: document.getElementById("hiddenUserId").value };
    console.log(parameter);
    fetch("/user/dvd/rent/history", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(parameter),
    })
      .then((response) => response.json())
      .then((response) => {
        let content = [];
        if (!response.data.length) {
          return;
        }
        for (let [index, record] of response.data.entries()) {
          let template = `
          <tr>
          <td>${index + 1}</td>
          <td>${record.start_date}</td>
          <td>${record.due_date}</td>
          <td>${record.title}</td>
          </tr>`;
          content.push(template);
        }

        document.getElementById("history_table").innerHTML = content.join("");
      });
  }
}
document.addEventListener("DOMContentLoaded", function () {
  new HistoryRent().render();
});
