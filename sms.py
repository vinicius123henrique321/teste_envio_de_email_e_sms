# EXEMPLO FUNCIONAL ABAIXO #




import pandas as pd
import os
from twilio.rest import Client

# passo a passo!

# abrir os 6 arquivos
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] >= 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] >= 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] >= 55000, "Vendas"].values[0]
        print(f"No mês de {mes} o vendedor {vendedor} vendeu um total de R${vendas} , ultrapassando a meta!") 

# Para cada arquivo:

# verificar SE algum valor algum valor na tabela de vendas é igual ou maior que 55.000

# se for maior que 55.000, enviar um sms com nome, mes e as vendas dele


account_sid = ' ' # para o account_sid e euth_token é preciso fazer uma conta no twilio!
auth_token = ' ' 
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= f"No mês de {mes} o vendedor {vendedor} vendeu um total de R${vendas} , ultrapassando a meta!",
                     from_=' ', #twilio também conesegue gerar um número para isso
                     to=' ' # aqui é só adicionar um número cadastrado!
                 )

print(message.sid)