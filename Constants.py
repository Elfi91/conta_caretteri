
# ================
# CONFIGURAZIONE COSTANTI
# ================

# Pattern                 | Descrizione
# ------------------------|--------------------------------------------
# .                       | Tutti i caratteri (con re.DOTALL include \n)
# \S                      | Caratteri senza spazi
# [a-zA-ZÀ-ÿ]             | Solo lettere (incluse accentate)
# \w+                     | Parole (lettere, numeri, underscore)
# [a-zA-ZÀ-ÿ]+            | Parole solo lettere (incluse accentate)
# [^.!?]+[.!?]+           | Frasi (testo seguito da punteggiatura)
# testo.split('\\n\\n')   | Paragrafi (separati da riga vuota)


# ===============================
#   REGEX PATTERNS -> Configurazioni e costanti *costanti si scrivono in maiuscolo*
# =============================== 

REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'    # Solo lettere, incluse accentate
REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?


# ===============================
# URL
# =============================== 
URL: str = "https://raw.githubusercontent.com/Elfi91/conta_caretteri/refs/heads/master/text.txt"
