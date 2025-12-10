from app.logic.analyzer import validazione, reverse, conteggio_nucleotidi, percentuale_coppie, trascrizione, traduzione
from app.logic.codons import codoni
from app.logic.amino_acids import amminoacidi

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# count = conteggio_nucleotidi(sequenza)
# print(f"Frequenza dei nucleotidi: {count}")


# sequenza = input("Inserisci la sequenza DNA: ").upper()
# percentuale = percentuale_coppie(sequenza)
# print(percentuale)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# trascritta = trascrizione(sequenza)
# print(trascritta)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# sequenza_verificata=validazione(sequenza)
# print(sequenza_verificata)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# complementare = reverse(sequenza)
# print(complementare)

sequenza = input("Inserisci la sequenza DNA: ").upper()
sequenza_tradotta=traduzione(sequenza)
print(sequenza_tradotta)


# sequenza = input("Inserisci la sequenza DNA: ").upper()
# sequenza_corretta=trascrizione(sequenza)
# codone_di_inizio="AUG"
# inidice_inizio=sequenza_corretta.find(codone_di_inizio)
# print(f" sequenza trascritta {sequenza_corretta}, indice : {inidice_inizio}, sequenza: {sequenza_corretta[inidice_inizio:]}")

# amminoacido = input("Inserisci la sequenza DNA: ")
# for key in amminoacidi.keys():
#  if amminoacido == key:
#   print(amminoacidi[key])
#   break
# else:
#   print("Amminoacido non trovato")
