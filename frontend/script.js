function viewAs(role) {
  document.getElementById("dashboard").innerHTML = `<h2>${role.toUpperCase()} Dashboard</h2>`;
  loadData(role);
}

function loadData(role) {
  fetch("http://127.0.0.1:8000/trends")
    .then(res => res.json())
    .then(data => {
      data.forEach(item => {
        let card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `<h3>${item.topic}</h3><p>Source: ${item.source}</p><p>Score: ${item.score}</p>`;
        document.getElementById("dashboard").appendChild(card);
      });
    });
}
