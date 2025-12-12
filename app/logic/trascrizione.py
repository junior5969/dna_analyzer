from app.logic.reverse import reverse

def trascrizione(sequenza):
    complementare = reverse(sequenza)
    sequenza_trascritta = complementare.replace("T", "U")
    return sequenza_trascritta
