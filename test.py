from app.logic.analyzer import validazione, reverse, conteggio_nucleotidi, percentuale_coppie, trascrizione, traduzione
from app.logic.codons import codoni

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

