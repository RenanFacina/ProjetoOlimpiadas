def QuemTemMaisMedalhas (caminho_csv):
    import pandas as pd
    import pymysql
    import ConexaoMySql

    # Leitura do arquivo CSV
    dados = pd.read_csv(caminho_csv, thousands=',')

    # Remover espaços em branco do nome das colunas
    dados.columns = dados.columns.str.strip()

    # --------------Pais com mais medalhas de Ouro Edição de Verão--------------------

    # Encontre a quantidade máxima de medalhas de ouro em uma edição de verão
    max_medalhas_ouro = dados["summer_gold"].max()

    # Encontre os países que têm a quantidade máxima de medalhas de ouro em uma edição de verão
    paises_max_ouro = dados[dados["summer_gold"] == max_medalhas_ouro]

    pais_max_ouro = paises_max_ouro["countries"].iloc[0]

    print(f"O país com mais medalhas de ouro de verão é: {pais_max_ouro}")
    print(f"Contendo {max_medalhas_ouro} medalhas de ouro")

    # --------------Pais com mais medalhas de Prata Edição de Verão--------------------

    # Encontre a quantidade máxima de medalhas de ouro em uma edição de verão
    max_medalhas_prata = dados["summer_silver"].max()

    # Encontre os países que têm a quantidade máxima de medalhas de ouro em uma edição de verão
    paises_max_prata = dados[dados["summer_silver"] == max_medalhas_prata]

    pais_max_prata = paises_max_prata["countries"].iloc[0]

    print(f"\nO país com mais medalhas de prata de verão é: {pais_max_prata}")
    print(f"Contendo {max_medalhas_prata} medalhas de prata")

    # --------------Pais com mais medalhas de bronze Edição de Verão--------------------

    # Encontre a quantidade máxima de medalhas de ouro em uma edição de verão
    max_medalhas_bronze = dados["summer_bronze"].max()

    # Encontre os países que têm a quantidade máxima de medalhas de ouro em uma edição de verão
    paises_max_bronze = dados[dados["summer_bronze"] == max_medalhas_bronze]

    pais_max_bronze = paises_max_bronze["countries"].iloc[0]

    print(f"\nO país com mais medalhas de bronze de verão é: {pais_max_bronze}")
    print(f"Contendo {max_medalhas_bronze} medalhas de bronze")

    try:
        ConexaoMySql.Conectar()

        cursor = ConexaoMySql.con.cursor()

        sql = '''
        UPDATE Analise
        SET
        pais_max_ouro_v = %s,
        max_medalhas_ouro_v = %s,
        pais_max_prata_v = %s,
        max_medalhas_prata_v = %s,
        pais_max_bronze_v = %s,
        max_medalhas_bronze_v = %s'''
        
        cursor.execute(sql, (
            pais_max_ouro,
            max_medalhas_ouro,
            pais_max_prata,
            max_medalhas_prata,
            pais_max_bronze,
            max_medalhas_bronze
        ))
        ConexaoMySql.con.commit()

    except pymysql.Error as e:
        print("Erro:", e)
    
    finally:
        cursor.close()
        ConexaoMySql.con.close()