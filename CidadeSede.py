def CidadeSede():

    # Crie um dicionário com o ano e a cidade-sede dos Jogos Olímpicos de Verão
    verao = {
        1896: "Atenas",
        1900: "Paris",
        1904: "St. Louis",
        1908: "Londres",
        1912: "Estocolmo",
        1920: "Antuérpia",
        1924: "Paris",
        1928: "Amsterdã/Amesterdão",
        1932: "Los Angeles",
        1936: "Berlim",
        1940: "",
        1944: "",
        1948: "Londres",
        1952: "Helsinque/Helsínquia",
        1956: "Melbourne",
        1960: "Roma",
        1964: "Tóquio",
        1968: "Cidade do México",
        1972: "Munique",
        1976: "Montreal",
        1980: "Moscou/Moscovo",
        1984: "Los Angeles",
        1988: "Seul",
        1992: "Barcelona",
        1996: "Atlanta",
        2000: "Sydney",
        2004: "Atenas",
        2008: "Pequim",
        2012: "Londres",
        2016: "Rio de Janeiro",
        2020: "Tóquio",
        2024: "Paris"
    }

    # Crie um dicionário para contar quantas vezes cada cidade sediou os Jogos
    cidades_sede = {}
    for cidade in verao.values():
        if cidade != "":
            if cidade in cidades_sede:
                cidades_sede[cidade] += 1
            else:
                cidades_sede[cidade] = 1

    # Encontre a(s) cidade(s) que mais sediou os Jogos
    max_sedes = max(cidades_sede.values())
    cidades_mais_sede = [cidade for cidade, sedes in cidades_sede.items() if sedes == max_sedes]

    print("Cidade(s) que mais sediou os Jogos Olímpicos de Verão:")
    for cidade in cidades_mais_sede:
        print(cidade)