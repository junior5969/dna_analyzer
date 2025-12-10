from app.logic.codons import codoni
from app.logic.amino_acids import amminoacidi

def validazione(sequenza):
 nucleotidi= "ATCG"
 for nucleotide in sequenza:
  if nucleotide not in nucleotidi:
   return None    
 return sequenza        

def somma_sequenze(sequenza1, sequenza2):
 sequenza1=validazione(sequenza1)
 sequenza2=validazione(sequenza2)
 somma= sequenza1 + sequenza2
 return somma

def conteggio_nucleotidi(sequenza):
  conteggio = {}
  sequenza=validazione(sequenza)
  for nucleotide in sequenza:
        if nucleotide in conteggio:
              conteggio[nucleotide] += 1
        else:
            conteggio[nucleotide] = 1
    
  return conteggio

def percentuale_coppie(sequenza):
 conteggio = conteggio_nucleotidi(sequenza)
 frequenza_a=conteggio["A"]
 frequenza_t=conteggio["T"]
 frequenza_c=conteggio["C"]
 frequenza_g=conteggio["G"]
 percentuale_at= f"{((frequenza_a+frequenza_t)/len(sequenza))*100} %"
 percentuale_cg= f"{((frequenza_c+frequenza_g)/len(sequenza))*100} %"
 percentuali={
    "Percentuale AT": percentuale_at,
    "Percentuale CG": percentuale_cg
 }
 return percentuali


def reverse(sequenza):
    sequenza=validazione(sequenza)

    if sequenza is None:
        return "Sequenza non valida!"
    
    conversione_nucleotidi = str.maketrans({
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
})

    sequenza_complementare = sequenza.translate(conversione_nucleotidi)
    return sequenza_complementare


def trascrizione(sequenza):
    complementare = reverse(sequenza)
    sequenza_trascritta = complementare.replace("T", "U")
    return sequenza_trascritta


def traduzione(sequenza):
 sequenza_trascritta = trascrizione(sequenza)
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
 return f"La sequenza complementare è {sequenza_trascritta} quella da tradurre è {sequenza_da_tradurre}, i codoni ottenuti sono {triplette}\n" + "\n".join(risultati) + f"\nGli amminoacidi risultanti sono: {proteina_str}"
#amminoacido -> indice della lista di valori -> chiave di quell'indice

