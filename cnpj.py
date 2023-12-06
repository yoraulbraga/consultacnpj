import requests, os

print("|" + "=" * 5 + "[Consulta CNPJ by @eu.raullopes]" + "=" * 5 + "|")
cnpj = input("CNPJ para Consulta, apenas numeros: ")
os.system("cls")

if cnpj.isnumeric():
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        cnpj_info = resposta.json()

        print(f'Nome: {cnpj_info['nome']}')
        print(f'Fantasia: {cnpj_info['fantasia']}')
        print(f'Natureza juridica: {cnpj_info['natureza_juridica']}')
        print(f'Status CNPJ: {cnpj_info['status']}')
        print(f'Situação: {cnpj_info['situacao']}')
        print(f'Data Situação: {cnpj_info['data_situacao']}')
        print(f'Motivo Situação: {cnpj_info['motivo_situacao']}')
        print(f'Tipo: {cnpj_info['tipo']}')
        print(f'Porte: {cnpj_info['porte']}')
        print(f'Abertura: {cnpj_info['abertura']}')
        print(f'CEP: {cnpj_info['cep']}')
        print(f'Municipio: {cnpj_info['municipio']}')
        print(f'UF: {cnpj_info['uf']}')
        print(f'Capital Social: {cnpj_info['capital_social']}')

        """atividades_principais = cnpj_info.get('atividade_principal', [])
        for atividade in atividades_principais:
            code = atividade.get('code')
            text = atividade.get('text')
        print(f'Codigo: {code}, Texto: {text}')"""
        
    elif resposta.status_code == 429:
        print("Muitas requisições, aguarde uns instantes.")
    else:
        print("Não conseguimos capturar informações.")
else:
    print("Apenas numeros.")
