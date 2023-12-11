import requests
import json
from pathlib import Path

# URL de l'API Hugging Face
api_url = "https://datasets-server.huggingface.co/rows?dataset=Ammok/apple_stock_price_from_1980-2021&config=default&split=train&offset=0&length=100"

# Exécuter la requête avec requests
response = requests.get(api_url)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    # Charger les données JSON
    data = response.json()

    # Sauvegarder les données dans un fichier JSON (par exemple)
    output_path = Path(__file__).resolve().parent / "hugging_face_data.json"
    with open(
        output_path, "w"
    ) as f:  # with garantit la fermeture auto du fichier même en cas d'erreur
        json.dump(data, f, indent=2)

    print(f"Données enregistrées avec succès dans {output_path}")
else:
    print(f"Échec de la requête. Code d'erreur : {response.status_code}")
