def SemMedalhas (caminho_csv):
    import pandas as pd
    import pymysql
    import ConexaoMySql

    # Leitura do arquivo CSV
    dados = pd.read_csv(caminho_csv, thousands=',')
    nunca_ganharam_ouro = 0
    nunca_ganharam_prata = 0
    nunca_ganharam_bronze = 0


    # Remover espaços em branco do nome das colunas e converter a coluna em números
    dados.columns = dados.columns.str.strip()
    dados["summer_gold"] = pd.to_numeric(dados["summer_gold"], errors='coerce')
    dados["summer_silver"] = pd.to_numeric(dados["summer_silver"], errors='coerce')
    dados["summer_bronze"] = pd.to_numeric(dados["summer_bronze"], errors='coerce')
    dados["winter_gold"] = pd.to_numeric(dados["winter_gold"], errors='coerce')
    dados["winter_silver"] = pd.to_numeric(dados["winter_silver"], errors='coerce')
    dados["winter_bronze"] = pd.to_numeric(dados["winter_bronze"], errors='coerce')

    print("Países que nunca ganharam medalha de ouro:\n")
    for index, row in dados.iterrows(): #método iterrows() para iterar sobre as linhas do DataFrame e verificar se cada país ganhou medalhas de ouro 
        pais = row["countries"]
        n_ganharam = row["summer_gold"] + row["winter_gold"]
        if n_ganharam <= 0:
            print(pais)
            nunca_ganharam_ouro = nunca_ganharam_ouro + 1

    print("\nPaíses que nunca ganharam medalha de prata:\n")
    for index, row in dados.iterrows(): #método iterrows() para iterar sobre as linhas do DataFrame e verificar se cada país ganhou medalhas de ouro 
        pais = row["countries"]
        n_ganharam = row["summer_silver"] + row["winter_silver"]
        if n_ganharam <= 0:
            print(pais)
            nunca_ganharam_prata = nunca_ganharam_prata + 1
            
    print("\nPaíses que nunca ganharam medalha de bronze:\n")
    for index, row in dados.iterrows(): #método iterrows() para iterar sobre as linhas do DataFrame e verificar se cada país ganhou medalhas de ouro 
        pais = row["countries"]
        n_ganharam = row["summer_bronze"] + row["winter_bronze"]
        if n_ganharam <= 0:
            print(pais)
            nunca_ganharam_bronze = nunca_ganharam_bronze + 1

    try:
        ConexaoMySql.Conectar()

        cursor = ConexaoMySql.con.cursor()

        sql = '''
        UPDATE Analise
        SET
        nunca_ganharam_ouro = %s,
        nunca_ganharam_prata = %s,
        nunca_ganharam_bronze = %s'''
        
        cursor.execute(sql, (
            nunca_ganharam_ouro,
            nunca_ganharam_prata,
            nunca_ganharam_bronze
        ))
        ConexaoMySql.con.commit()

    except pymysql.Error as e:
        print("Erro:", e)
    
    finally:
        cursor.close()
        ConexaoMySql.con.close()