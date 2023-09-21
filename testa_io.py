arquivo =  open('dados/contatos_escrita.csv', encoding='utf-8', mode='a+')


print(type(arquivo.buffer))

# conteudo = arquivo.buffer.read()

texto_em_bytes = bytes('esse é um texto em bytes', 'utf-8')
# print(texto_em_bytes)
contato = bytes('15,Veronica,veronica@veronica.com.br\n', 'utf-8')
arquivo.buffer.write(contato)

arquivo.close()

