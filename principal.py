from contatos_utils import csv_para_contatos, contatos_para_pickle, pickle_para_contatos, contatos_para_json, json_para_contatos

try:
    # contatos = csv_para_contatos('dados/contatos.csv', 'utf-8')
    # contatos_para_pickle(contatos, 'dados/contatos.p')
    # contatos = pickle_para_contatos('dados/contatos.p')
    # contatos_para_json(contatos,'dados/contatos.json')
    contatos = json_para_contatos('dados/contatos.json')
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print("Arquivo não encontrado!!")
except PermissionError:
    print("Sem Permissão de escrita!!")
