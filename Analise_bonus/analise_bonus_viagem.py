import pandas as pd
from twilio.rest import Client

account_sid = "AC1f1506e8b2fa2d9e687e49c2a2f2919c"
auth_token  = "77b112bd96381971ce8f7f8038004701"
client = Client(account_sid, auth_token)

lista_meses = ['abril','fevereiro', 'janeiro', 'junho', 'maio']

for mes in lista_meses:
    tabela_vendas = pd.read_excel('{}.xlsx'.format(mes))
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f"No mes {mes} encontrou alguem com mais de 55000. Vendedor: {vendedor}, Vendas {vendas}")
        message = client.messages.create(
            to="+5561999350743", 
            from_="+13023053926",
            body=f"No mes {mes} encontrou alguem com mais de 55000. Vendedor: {vendedor}, Vendas {vendas}")
        print(message.sid)


