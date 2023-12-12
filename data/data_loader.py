import requests
import pandas as pd
from pathlib import Path

# URL de base
base_url = "https://datasets-server.huggingface.co/rows?dataset=Ammok/apple_stock_price_from_1980-2021&config=default&split=train"

# Preparing loop's parameters
response = requests.get(base_url)
data = response.json()
total_line = data['num_rows_total'] # we could request directly num_rows with the hugg_face params size but with this way we economize the first loading
df = pd.json_normalize(data['rows'])  # initialiser la transformation des data en csv

q = total_line // 100
r = total_line % 100
n_iter = q if r==0 else q + 1

# loading data sequentially
for i in range(1,n_iter) :  # commence à 1 car on aura déjà fait au moins un request pour obtenir le total_line même s'il est nul
    offset = i*100
    api_url = f"{base_url}&offset={offset}&length=100"
    response = requests.get(api_url)
    data = response.json()
    df = pd.concat([df,pd.json_normalize(data['rows'])], axis = 0, ignore_index = True)

df=df.drop(['row_idx','truncated_cells'], axis = 1)

# sortie
output_dir = Path("%pwd").resolve().parent
output_path = output_dir / "hugging_face_data.csv"
data_csv = df.to_csv(output_path, index=False)
