
def validazione(sequenza):
 nucleotidi= "ATCG"
 if nucleotidi not in sequenza:
  return "La sequenza non è valida"   
 else:
   return f"La sequenza è valida: {sequenza }"        

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
    conversione_nucleotidi = str.maketrans({
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
})
    sequenza_complementare = sequenza.translate(conversione_nucleotidi)
    return sequenza_complementare


def trascrizione(sequenza):
    sequenza_complementare = reverse(sequenza)
    sequenza_trascritta = sequenza_complementare.replace("T", "U")
    sequenze= {
        "Sequenza Complementare": sequenza_complementare,
        "Sequenza Trascritta (RNA)": sequenza_trascritta
    }
    return sequenze