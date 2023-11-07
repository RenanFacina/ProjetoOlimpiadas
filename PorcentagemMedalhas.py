def PorcentagemMedalhas (caminho_csv):
    import pandas as pd

    # Leitura do arquivo CSV
    dados = pd.read_csv(caminho_csv, thousands=',')

    # Titulo
    print("Porcentagem de Medalhas por País")

    # Inserir o país
    pais = input("\nDigite o país desejado (em Inglês): ")

    # Remover espaços em branco do nome das colunas e converter a coluna "total_total" em números
    dados.columns = dados.columns.str.strip()
    dados['total_total'] = pd.to_numeric(dados['total_total'], errors='coerce')

    # Verificar se o país está na lista de países disponíveis
    if pais in dados['countries'].unique():
        
        # Seleciona o pais da coluna "countries"
        pais_desejado = dados[dados['countries'] == pais]

        # Medalhas totais do pais selecionado
        medalhas_pais = pais_desejado["total_total"].sum()

        # Calcula a soma total de medalhas
        soma_medalhas = dados["total_total"].sum()

        # Calcula a porcentagem de medalhas do pais escolhido
        porcentagem = (medalhas_pais / soma_medalhas) * 100

    # Resultados
        print(f"\n{pais} tem {medalhas_pais} medalhas")
        print(f"A porcentagem de medalhas do país {pais} é: {porcentagem:.2f}%")

    else:
        print(f"\n{pais} é um país inválido.\nEscolha um país válido ou verifique a ortografia e se está em Inglês.")
