from app.logic.trascrizione import trascrizione
from app.logic.codons import codoni
from app.logic.amino_acids import amminoacidi

def traduzione(sequenza):
    sequenza_trascritta = trascrizione(sequenza)
    codone_di_inizio="AUG"
    inidice_codone_di_inizio = sequenza_trascritta.find(codone_di_inizio)
    sequenza_da_tradurre = sequenza_trascritta[inidice_codone_di_inizio:]
    triplette = []
    for nucleotide in range(0, len(sequenza_da_tradurre), 3):
        triplette.append(sequenza_da_tradurre[nucleotide:nucleotide+3])

    risultati = []

    for t in triplette:
        fermati = False
        for codone in codoni.values():
            for tripletta in codone:
                if t == tripletta:
                    amminoacido = list(codoni.keys())[list(codoni.values()).index(codone)]
                    risultati.append(amminoacido)
                    if amminoacido == "Stop":
                        fermati = True
                        break
            if fermati:
                break
        if fermati:
            break

    proteina = []
    for key in amminoacidi.keys():
        for a in risultati:
            if a == key:
                sigla_amminoacido = amminoacidi[key]
                proteina.append(sigla_amminoacido)
    proteina_str = ''.join(proteina)
    return f"La sequenza complementare è {sequenza_trascritta} quella da tradurre è {sequenza_da_tradurre}, i codoni ottenuti sono {triplette} e gli amminoacidi risultanti sono: {proteina_str}"
