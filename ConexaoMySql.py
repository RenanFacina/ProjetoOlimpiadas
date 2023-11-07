def Conectar():
    import pymysql
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        database='OlimpiadasDatabase',
        passwd='1234',
        cursorclass=pymysql.cursors.DictCursor
    )