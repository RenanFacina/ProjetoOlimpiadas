# Pais que não ganharam medalhas e seu respectivos anos
data = """Afghanistan,(AFG),15,0,0,2,2,0,0,0,0,0,15,0,0,2,2
Algeria,(ALG),14,5,4,8,17,3,0,0,0,0,17,5,4,8,17
Argentina,(ARG),25,21,26,30,77,20,0,0,0,0,45,21,26,30,77
... (resto dos dados) ..."""

linhas = data.split('\n')


medalhas_por_pais = {}


for linha in linhas:
    partes = linha.split(',')
    pais = partes[0]
    medalhas = [int(partes[i]) for i in range(2, len(partes))]
    medalhas_por_pais[pais] = medalhas


paises_sem_medalhas = [pais for pais, medalhas in medalhas_por_pais.items() if sum(medalhas) == 0]

# Imprima a lista de países que nunca ganharam medalhas
for pais in paises_sem_medalhas:
    print(pais)
