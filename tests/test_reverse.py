from app.logic.reverse import reverse, reverse_string

def test_reverse():
    seq = "AGCTAG"

    complementare = reverse(seq)
    risultato = reverse_string(complementare)

    assert risultato == "La sequenza complementare è: TCGATC"
