document.addEventListener("DOMContentLoaded", function () {
  const bottoni = document.querySelectorAll(".button");
  const bottoneInput = document.querySelector(".bottone-input");

  bottoni.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();  // previene il submit del form classico

      const input = document.querySelector("#input-sequenza");
      const sequenza = input.value.trim().toUpperCase();

      fetch("/analizza", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sequenza: sequenza, azione: btn.dataset.azione }),
      })
        .then((response) => response.json())
        .then((result) => {
          if (result.risultato) {
        document.getElementById("risultato").textContent = result.risultato;
          } else if (result.errore) {
            document.getElementById("risultato").textContent =
              "Errore: " + result.errore;
          }
        })
        .catch((error) => {
          document.getElementById("risultato").textContent =
            "Errore durante l'invio";
          console.error("Errore:", error);
        });
    });
  });



    bottoneInput.addEventListener("click", (e) => {
      e.preventDefault();  // previene il submit del form classico

      const inputDNA = document.querySelector("#input-sequenza");
      const sequenza = inputDNA.value.trim().toUpperCase();
      const inputMotivo = document.querySelector("#input-sequenza-motivo");
      const motivo = inputMotivo.value.trim().toUpperCase();

      fetch("/analizza", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sequenza: sequenza, motivo:motivo, azione: bottoneInput.dataset.azione }),
      })
        .then((response) => response.json())
        .then((result) => {
          if (result.risultato) {
        document.getElementById("risultato").textContent = result.risultato;
          } else if (result.errore) {
            document.getElementById("risultato").textContent =
              "Errore: " + result.errore;
          }
        })
        .catch((error) => {
          document.getElementById("risultato").textContent =
            "Errore durante l'invio";
          console.error("Errore:", error);
        });
    });
  });

