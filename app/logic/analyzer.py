from app.logic.codons import codoni
from app.logic.amino_acids import amminoacidi

def validazione(sequenza):
  nucleotidi= "ATCG"
  for nucleotide in sequenza:
   if nucleotide not in nucleotidi:
    return None  
  return sequenza        


def somma_sequenze(sequenza1, sequenza2):
  sequenza1_valida=validazione(sequenza1)
  sequenza2_valida=validazione(sequenza2)
  if sequenza1_valida is None or sequenza2_valida is None:
    return "Sequenza non valida"
  somma= sequenza1_valida + sequenza2_valida
  return somma


def conteggio_nucleotidi(sequenza):
  sequenza=validazione(sequenza)
  if sequenza is None:
    return "Sequenza non valida"
  conteggio = {}

  for nucleotide in sequenza:
        if nucleotide in conteggio:
              conteggio[nucleotide] += 1
        else:
            conteggio[nucleotide] = 1
  frequenza_a = conteggio.get("A", 0)
  frequenza_t = conteggio.get("T", 0)
  frequenza_c = conteggio.get("C", 0)
  frequenza_g = conteggio.get("G", 0)
  return f"L'Adenina (A) è presente {frequenza_a} volte, la Timina (T) è presente {frequenza_t} volte, la Guanina (G) è presente {frequenza_g} volte e la Citosina (C) è presente {frequenza_c} volte."


def percentuale_coppie(sequenza):
 sequenza= validazione(sequenza)
 if sequenza is None:
    return "Sequenza non valida"    
 conteggio = {"A": 0, "T": 0, "C": 0, "G": 0}
 for n in sequenza:
    conteggio[n] += 1
 frequenza_a=conteggio["A"]
 frequenza_t=conteggio["T"]
 frequenza_c=conteggio["C"]
 frequenza_g=conteggio["G"]
 percentuale_at= round((((frequenza_a+frequenza_t)/len(sequenza) )*100),2)
 percentuale_cg= round((((frequenza_c+frequenza_g)/len(sequenza))*100),2)
 return (f"La percentuale di AT è : {percentuale_at}%, quella di CG è : {percentuale_cg}%")


def reverse(sequenza):
    sequenza_validata=validazione(sequenza)
    if sequenza_validata is None:
      return "Sequenza non valida"

    conversione_nucleotidi = str.maketrans({
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
})
    sequenza_complementare = sequenza_validata.translate(conversione_nucleotidi)
    return sequenza_complementare


def trascrizione(sequenza):
    complementare = reverse(sequenza)
    if complementare == "Sequenza non valida":
        return "Sequenza non valida"

    sequenza_trascritta = complementare.replace("T", "U")
    return f"La sequenza che si ottiene dalla trascrizione è: {sequenza_trascritta}"


def traduzione(sequenza):
 sequenza_trascritta = trascrizione(sequenza)
 if sequenza_trascritta == "Sequenza non valida":
        return "Sequenza non valida"
 
 codone_di_inizio="AUG"
 inidice_codone_di_inizio=sequenza_trascritta.find(codone_di_inizio)
 sequenza_da_tradurre=sequenza_trascritta[inidice_codone_di_inizio:]
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
     sigla_amminoacido=(amminoacidi[key])
     proteina.append(sigla_amminoacido)
 proteina_str = ''.join(proteina)
 return f"La sequenza complementare è {sequenza_trascritta} quella da tradurre è {sequenza_da_tradurre}, i codoni ottenuti sono {triplette} e gli amminoacidi risultanti sono: {proteina_str}"
#amminoacido -> indice della lista di valori -> chiave di quell'indice

