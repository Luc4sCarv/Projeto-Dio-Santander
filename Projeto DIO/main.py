import pandas as pd
import random

def gerar_descricao_marketing(nome, categoria, preco):

    adjetivos = ["incrível", "essencial", "revolucionário", "imperdível"]
    beneficios = [
        "para melhorar o seu dia a dia.",
        "com o melhor custo-benefício do mercado.",
        "que você estava procurando."
    ]
    
    frase_simulada = f"Conheça o {nome}: um item {random.choice(adjetivos)} {random.choice(beneficios)}"
    return frase_simulada

print(">>> [E] Iniciando Extração dos dados...")
try:
    df = pd.read_csv('produtos.csv')
    print(f"Sucesso! {len(df)} produtos carregados.")
 
    print(df.head())
except FileNotFoundError:
    print("ERRO: O arquivo 'produtos.csv' não foi encontrado. Crie o arquivo antes de rodar.")
    exit()

print("\n>>> [T] Iniciando Transformação...")

df['Descricao_Marketing'] = df.apply(
    lambda row: gerar_descricao_marketing(row['Nome_Produto'], row['Categoria'], row['Preco']), 
    axis=1
)

print("Transformação concluída! Amostra dos dados gerados:")
print(df[['Nome_Produto', 'Descricao_Marketing']].head())

print("\n>>> [L] Iniciando Carregamento (Salvando arquivos)...")

df.to_csv('produtos_com_descricao.csv', index=False)

print("Processo finalizado! Arquivo 'produtos_com_descricao.csv' gerado com sucesso.")