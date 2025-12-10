# CONTACARATTERI

# DOMINIO:
# =========

# 1. INPUT - Sorgente del testo
#    - Lettura da file di testo (.txt)
#    - Visualizzazione contenuto in console

# 2. ELABORAZIONE - Metriche da calcolare
#   - Conteggio caratteri (con e senza spazi)
#   - Conteggio parole
#   - Conteggio frasi
#   - Conteggio paragrafi
#   - Tempo di lettura stimato
#   - Frequenza parole e lettere (ripetizioni)

# 3. OUTPUT - Destinazione risultati
#    - Stampa in console
#    - Scrittura su file

# ===============================
#   TODO 
# =============================== 

# 1. Migliorare gestione delle eccezioni
# 2. Unificare gestione stream e buffer dati 
# 3. Suddividere in moduli


from ui.console import print_risultato
from data.services import get_caratteri_len, get_phrase_number, get_text_len_no_space, get_words_number
from data.repository import get_data_from_server
from Constants import URL

def main() -> None:
    try:
        # content: str = get_file_content("text.txt")
        content: str = get_data_from_server(URL)
        print_risultato(get_caratteri_len(content), "caratteri")
        print_risultato(get_text_len_no_space(content), "caratteri senza spazi")
        print_risultato(get_words_number(content), "parole")
        print_risultato(get_phrase_number(content), "frasi")


    except ValueError as e:
        print(f"{e}")

    except FileNotFoundError as e:
        print(f"{e}")

    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()