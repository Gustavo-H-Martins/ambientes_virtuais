# ler todos os arquivos csv do diretório e guardar em um objeto
import numpy as np
import time
import os
import re
import pandas as pd
from datetime import datetime
from backup_limpeza import backup_limpeza_simples

datazip = f'{datetime.now().year}-{datetime.now().month-1}'
# realiza backup dos dados antigos
base_csv_estabelecimentos = r'../base_csv_estabelecimentos/'
all_files_estabelecimentos = list(filter(lambda x: '.csv' in x, os.listdir(base_csv_estabelecimentos)))
if len(all_files_estabelecimentos) >= 1:
    backup_limpeza_simples(pasta=base_csv_estabelecimentos, nome_zipado=f'base_csv_estabelecimentos{datazip}.zip',extensao='.csv')
#diretorio = r'Bases\Base_atualizada/'
diretorio = r'C:\Users\ABRASEL NACIONAL\Documents\CNPJ_PROGRAMATICA\Manipulacao_arquivos\Manipulacao_Arquivos_Python\Bases/'
all_files = list(filter(lambda x: '.csv' in x, os.listdir(diretorio)))

#Warnings: Possui uma série de funções e comandos para tratamento de mensagens de avisos e alertas do Python
import warnings
warnings.filterwarnings("ignore")

# definindo colunas e tipos
ESTABELE = ['CNPJ_BASE', 'CNPJ_ORDEM', 'CNPJ_DV', 'MATRIZ_FILIAL', 'NOME_FANTASIA',
       'SITUACAO_CADASTRAL', 'DATA_SITUACAO_CADASTRAL',
       'MOTIVO_SITUACAO_CADASTRAL', 'DATA_INICIO_ATIVIDADE', 'CNAE_PRINCIPAL',
       'CNAE_SECUNDARIO', 'TIPO_LOGRADOURO', 'LOGRADOURO', 'NUMERO',
       'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'MUNICIPIO', 'TELEFONE1',
       'TELEFONE2', 'FAX', 'EMAIL']

dtypes = {'CNPJ_BASE': 'category',
 'CNPJ_ORDEM': 'category',
 'CNPJ_DV': 'category'}

# Define CNAES
CNAES = {5611201:'Restaurantes e similares',
        5611203:'Lanchonetes casas de chá de sucos e similares',
        5611204:'Bares e outros estabelecimentos especializados em servir bebidas sem entretenimento',
        5611205:'Bares e outros estabelecimentos especializados em servir bebidas com entretenimento',
        5612100: 'Serviços ambulantes de alimentação'}
lista_cnae = []
lista_descricao = []
for cnae in CNAES.keys():
    lista_cnae.append(cnae)
for descricao in CNAES.values():
    lista_descricao.append(descricao)

# processa os dados
c = 0
for file in all_files:
    dados =pd.read_csv(f'{diretorio}{file}', names=ESTABELE, dtype=dtypes, sep=';')
    dados['CNAE_DESCRICAO'] = lista_descricao[c]
    dados = dados[[
        'CNPJ_BASE', 'CNPJ_ORDEM', 'CNPJ_DV', 'NOME_FANTASIA', 'CNAE_PRINCIPAL','CNAE_DESCRICAO',
        'TIPO_LOGRADOURO', 'LOGRADOURO', 'NUMERO',
       'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'MUNICIPIO', 'TELEFONE1']]
    c +=1
    dados.to_csv(f"../base_csv_estabelecimentos/{file}", mode='w',index=False, sep=';')
