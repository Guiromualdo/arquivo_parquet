from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/cidade")
def get_city_residents(nome: str):
    df = pd.read_parquet("dados.parquet")
    # Busca parcial: retorna cidades que contêm o texto fornecido (case-insensitive)
    city_residents = df[df["city"].str.lower().str.contains(nome.lower())]
    return city_residents.to_dict(orient="records")