import json

log = "-- LOG DO SISTEMA --\n"
log += "Lendo log...\n"

arquivo = open('dados.json', 'r')
info = arquivo.read()
# print(info)

dados = json.loads(info)

log += "Alterando chave 'color' para 'red'"
dados['color'] = "red"

log += "Gravando novo arquivo...\n"
novo_arquivo = open('dados_novo.json', 'w')
novos_dados = json.dumps(dados)
novo_arquivo.write(novos_dados)
novo_arquivo.close()

log += "Adicionando novo arquivo\n"
novo_arquivo = open('dados_novo.json', 'a')
novo_arquivo.write(', { "new": "yes" }')
novo_arquivo.close()

novo_log = open('log.txt', 'w')
novo_log.write(log)
novo_log.close()
