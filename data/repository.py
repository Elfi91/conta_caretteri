# ===============================
#   Repository
# =============================== 

def get_file_content(file_path: str) -> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")
   
    try:
        with open(file_path, "r") as f:
            return f.read()       
   
    except FileNotFoundError:
        raise FileNotFoundError("il file non esiste")

import requests

def get_data_from_server(url: str) -> str:
    if not url or not isinstance(url, str):
        raise ValueError("L'url deve essere una stringa non vuota")
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        raise Exception("Problema con la chiamata")