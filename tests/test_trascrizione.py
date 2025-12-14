from app.logic.trascrizione import trascrizione, trascrizione_string
from app.logic.reverse import reverse

def test_trascrizione():
    seq="AGCTAG"
    complementare = reverse(seq)
    trascritta=trascrizione(seq)
    risultato=trascrizione_string(complementare, trascritta)

    assert risultato == "La sequenza complementare è: TCGATC e quella trascritta è: UCGAUC" 
