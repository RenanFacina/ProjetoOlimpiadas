def Participacao (caminho_csv):
    import pandas as pd
    import pymysql
    import ConexaoMySql

    dados = pd.read_csv(caminho_csv, thousands=',')

    pais_com_mais_participacao_verao = dados.loc[dados['summer_participations'].idxmax()]['countries']
    max_participacao_verao = dados['summer_participations'].max()
    print(f"País com maior participação no verão: {pais_com_mais_participacao_verao} ({max_participacao_verao} participações.)")

    pais_com_mais_participacao_inverno = dados.loc[dados['winter_participations'].idxmax()]['countries']
    max_participacao_inverno = dados['winter_participations'].max()

    print(f"País com maior participação no inverno: {pais_com_mais_participacao_inverno} ({max_participacao_inverno} participações.)")

    pais_com_mais_participacao = dados.loc[dados['total_participation'].idxmax()]['countries']
    max_participacao = dados['total_participation'].max()
    print(f"País com maior participação total: {pais_com_mais_participacao} ({max_participacao} participações.)")

    pais_com_menos_participacao = dados.loc[dados['total_participation'].idxmin()]['countries']
    menos_participacao = dados['total_participation'].min()
    print(f"País com a menor participação total: {pais_com_menos_participacao} ({menos_participacao} participações.)")

    try:
        ConexaoMySql.Conectar()

        cursor = ConexaoMySql.con.cursor()

        sql = '''
        UPDATE Analise
        SET
        pais_com_mais_participacao_v = %s,
        pais_com_mais_participacao_i = %s,
        pais_com_mais_participacao = %s,
        pais_com_menos_participacao = %s'''
        
        cursor.execute(sql, (
            pais_com_mais_participacao_verao,
            pais_com_mais_participacao_inverno,
            pais_com_mais_participacao,
            pais_com_menos_participacao
        ))
        ConexaoMySql.con.commit()

    except pymysql.Error as e:
        print("Erro:", e)
    
    finally:
        cursor.close()
        ConexaoMySql.con.close()