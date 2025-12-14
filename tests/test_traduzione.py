from app.logic.traduzione import traduzione

def test_traduzione():
    seq="TACGGGTTT"
    risultato=traduzione(seq)
    assert "La sequenza che si ottiene dalla trascrizione è: AUGCCCAAA, i codoni ottenuti sono: AUG, CCC, AAA e gli amminoacidi risultanti sono: MPK" in risultato

