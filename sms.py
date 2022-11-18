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
account_sid = 'ACce2d99f06f2e0fd4a02bb0cd27e23236'
auth_token = '00155c698412e7a75e4401e5367b4ea2'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= f"No mês de {mes} o vendedor {vendedor} vendeu um total de R${vendas} , ultrapassando a meta!",
                     from_='+15139603382',
                     to='+5512996719779'
                 )

print(message.sid)