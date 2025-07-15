import pandas as pd

try:
    df = pd.read_parquet("dados.parquet")
    print("Colunas do arquivo:", df.columns.tolist())
    print("\nTodos os valores únicos de city:")
    print(df["city"].unique())
except Exception as e:
    print("Ocorreu um erro:", e)