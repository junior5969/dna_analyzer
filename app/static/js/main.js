document.addEventListener("DOMContentLoaded", function () {
  const bottoni = document.querySelectorAll(".button");
  const bottoneInput = document.querySelector(".bottone-input");


  function sendRequest({ sequenza, motivo = null, azione }) {
    const body = { sequenza, azione };
    if (motivo) body.motivo = motivo; 

    fetch("/analizza", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    })
      .then((response) => response.json())
      .then((result) => {
        const risultatoEl = document.getElementById("risultato");
        if (result.risultato) {
          risultatoEl.textContent = result.risultato;
        } else if (result.errore) {
          risultatoEl.textContent = "Errore: " + result.errore;
        }
      })
      .catch((error) => {
        document.getElementById("risultato").textContent =
          "Errore durante l'invio";
        console.error("Errore:", error);
      });
  }

  
  bottoni.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const sequenza = document
        .querySelector("#input-sequenza")
        .value.trim()
        .toUpperCase();

      sendRequest({ sequenza, azione: btn.dataset.azione });
    });
  });


  bottoneInput.addEventListener("click", (e) => {
    e.preventDefault();
    const sequenza = document
      .querySelector("#input-sequenza")
      .value.trim()
      .toUpperCase();
    const motivo = document
      .querySelector("#input-sequenza-motivo")
      .value.trim()
      .toUpperCase();

    sendRequest({ sequenza, motivo, azione: bottoneInput.dataset.azione });
  });
});
