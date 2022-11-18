# EXEMPLO FUNCIONAL ABAIXO #




import pandas as pd
import win32com.client as win32

# importar database
tabela_vendas = pd.read_excel("Vendas.xlsx") 
# troque o excel do read_ caso queira ler outra coisa!

# visualizar a base de dados 
pd.set_option("display.max_columns", None)
print(tabela_vendas)

# faturamento por loja
# tabela_vendas[["ID Loja","Valor Final"]] = # filtro
# tabela_vendas.groupby("ID Loja").sum() = # agrupamento e soma 
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum() # conjunto dos ultimos
print(faturamento)

print("-" * 50)

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade) 

print("-" * 50)

# ticket médio por produto em cada loja
ticket_medio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "ticket"})
print(ticket_medio)

#enviar um email com o relatório ((código padrão para enviar os formulários por email (pip install pywin32))

outlook = win32.Dispatch("outlook.application")
mail = outlook.CreateItem(0)
mail.To = "vinihsr@hotmail.com"
mail.Subject = "Relatório de vendas por loja"
mail.HTMLBody = f'''
<p>Olá</p>

<p>Segue o relatório de vendas por cada loja:</p>

<p>faturamento:</p>
{faturamento.to_html(formatters={"Valor Final": "R${:,.2f}".format})}

<p>Quantidade:</p>
{quantidade.to_html()}

<p>Ticket médio dos produtos em cada loja:</p>
{ticket_medio.to_html(formatters={"ticket": "R${:,.2f}".format})}

<p>att.</p>
<p>Vinicius.</p>
'''

mail.Send()

print("Email enviado!")