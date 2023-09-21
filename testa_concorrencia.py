contato_carol = '11,Carol,carol@carol.com.br\n'
contatod_andreza = '12,Andreza,andreza@andreza.com.br\n'

with open('dados/contatos_escrita.csv', encoding='utf-8', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('dados/contatos_escrita.csv', encoding='utf-8', mode='a') as arquivo2:
    arquivo2.write(contatod_andreza)


arquivo1.close()
arquivo2.close()