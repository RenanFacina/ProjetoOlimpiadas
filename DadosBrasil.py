#Dados do Brasil nos jogos
def DadosBrasil (caminho_csv):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import pymysql
    import ConexaoMySql

    dados = pd.read_csv(caminho_csv, thousands=',')

    columns = {'countries ': 'country', 'ioc_code ': 'ioc_code',
                    'total_total ': 'total_total'}
    dados.rename(columns = columns, inplace=True)
    dados.columns

    # Dados do Brasil nos jogos ---------------------------------------------------------    

    print("\nEstatisticas do Brasil nos jogos:")
    # Verão
    brasil = pd.DataFrame(dados.iloc[16,:]).reset_index()
    bra_part_ver = brasil.iloc[2, 1] # numero de participações
    print("Numero de participações do Brasil nos jogos de verão: ", bra_part_ver)
    bra_ouro_v = brasil.iloc[3, 1] # numero de medalhas de ouro
    print("Numero de medalhas de ouro nos jogos de verão: ", bra_ouro_v)
    bra_prata_v = brasil.iloc[4, 1] # numero de medalhas de prata
    print("Numero de medalhas de prata nos jogos de verão: ", bra_prata_v)
    bra_bronze_v = brasil.iloc[5, 1] # numero de medalhas de bronze
    print("Numero de medalhas de bronze nos jogos de verão: ", bra_bronze_v)

    # Inverno
    brasil = pd.DataFrame(dados.iloc[16,:]).reset_index()
    bra_part_inv = brasil.iloc[7, 1] # numero de participações
    print("Numero de participações do Brasil nos jogos de inverno: ", bra_part_inv)
    bra_ouro_i = brasil.iloc[8, 1] # numero de medalhas de ouro
    print("Numero de medalhas de ouro nos jogos de inverno: ", bra_ouro_i)
    bra_prata_i = brasil.iloc[9, 1] # numero de medalhas de prata
    print("Numero de medalhas de prata nos jogos de verão: ", bra_prata_i)
    bra_bronze_i = brasil.iloc[10, 1] # numero de medalhas de ouro
    print("Numero de medalhas de bronze nos jogos de inverno: ", bra_bronze_i)

    try:
        ConexaoMySql.Conectar()

        cursor = ConexaoMySql.con.cursor()

        sql = '''
        UPDATE Analise
        SET
        bra_part_v = %s,
        bra_ouro_v = %s,
        bra_bronze_v = %s,
        bra_part_i = %s,
        bra_ouro_i = %s,
        bra_bronze_i = %s'''
        
        cursor.execute(sql, (
            bra_part_ver,
            bra_ouro_v,
            bra_bronze_v,
            bra_part_inv,
            bra_ouro_i,
            bra_bronze_i
        ))
        ConexaoMySql.con.commit()

    except pymysql.Error as e:
        print("Erro:", e)
        
    finally:
        cursor.close()
        ConexaoMySql.con.close()

    # Gráfico de barras com os dados

    # dados da Coréia do Sul
    korea = pd.DataFrame(dados.iloc[74,:]).reset_index()
    k_ouro_v = korea.iloc[3, 1]
    k_prata_v = korea.iloc[4, 1]
    k_bronze_v = korea.iloc[5, 1]

    x = ['Brasil', 'Coréia do Sul']
    # listas para cada plot
    y = [float(bra_bronze_v), float(k_bronze_v)]
    w = [float(bra_prata_v), float(k_ouro_v)]
    z = [float(bra_ouro_v), float(k_prata_v)]

    #teste
    #y = [1, 2, 3]
    #w = [2, 3, 4]
    #z = [3, 4, 5]

    ax = plt.subplot()
    ax.bar(x, y, width = 0.3, color = 'darkgoldenrod', label = 'Bronze')
    ax.bar(x, w, width = 0.3, color = 'orange', label = 'Prata')
    ax.bar(x, z, width = 0.3, color = 'navajowhite', label = 'Ouro')
    # muda quatidade de ticks no eixo Y
    plt.locator_params(axis = 'y', nbins = 12) 
    ax.set_title('Brasil em comparação com Coréia do Sul\nnos Jogos de Verão')
    plt.ylabel("Quantidade")
    plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))

    plt.show()