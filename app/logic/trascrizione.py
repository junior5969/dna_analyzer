from app.logic.reverse import reverse

def trascrizione(sequenza):
    complementare = reverse(sequenza)
    sequenza_trascritta = complementare.replace("T", "U")
    return sequenza_trascritta

def trascrizione_string(complementare, sequenza_trascritta):
    return f"La sequenza complementare è: {complementare} e quella trascritta è: {sequenza_trascritta}"
