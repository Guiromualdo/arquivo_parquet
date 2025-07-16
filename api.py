from fastapi import FastAPI
import pandas as pd
from typing import Optional
import random

app = FastAPI()

@app.get("/pessoas")
def get_pessoas(
    cidade: Optional[str] = None,
    sexo: Optional[str] = None,
    idade_min: Optional[int] = None,
    idade_max: Optional[int] = None,
    estado: Optional[str] = None,
    ocupacao: Optional[str] = None,
    nivel_educacao: Optional[str] = None,
    page: int = 1,
    per_page: int = 10,
    random: bool = False
):
    df = pd.read_parquet("dados.parquet")
    
    
    filtered_df = df.copy()

   
    if cidade:
        filtered_df = filtered_df[filtered_df["city"].str.lower().str.contains(cidade.lower())]
    if sexo:
        filtered_df = filtered_df[filtered_df["sex"].str.lower() == sexo.lower()]
    if idade_min is not None:
        filtered_df = filtered_df[filtered_df["age"] >= idade_min]
    if idade_max is not None:
        filtered_df = filtered_df[filtered_df["age"] <= idade_max]
    if estado:
        filtered_df = filtered_df[filtered_df["state"].str.lower() == estado.lower()]
    if ocupacao:
        filtered_df = filtered_df[filtered_df["occupation"].str.lower() == ocupacao.lower()]
    if nivel_educacao:
        filtered_df = filtered_df[filtered_df["education_level"].str.lower() == nivel_educacao.lower()]

 
    if random and not filtered_df.empty:
        random_idx = random.randint(0, len(filtered_df) - 1)
        paginated_df = filtered_df.iloc[[random_idx]]
        total_items = 1
        page = 1
        per_page = 1
        total_pages = 1
    else:
        total_items = len(filtered_df)
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_df = filtered_df.iloc[start_idx:end_idx]
        total_pages = (total_items + per_page - 1) // per_page

    return {
        "data": paginated_df.to_dict(orient="records"),
        "total_items": total_items,
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages
    }

@app.get("/pessoa/{uuid}")
def get_pessoa(uuid: str):
    df = pd.read_parquet("dados.parquet")
    pessoa = df[df["uuid"] == uuid]
    if len(pessoa) == 0:
        return {"error": "Pessoa não encontrada"}
    return pessoa.iloc[0].to_dict()