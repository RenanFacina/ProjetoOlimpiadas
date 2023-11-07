import DadosBrasil
import PorcentagemMedalhas
import QuemTemMaisMedalhas
import Participacao
import SemMedalhas
import CidadeSede

def main():
    caminho_csv = "DataSet/olympics_medals_country_wise.csv"

    while True:
        print("\nSelecione a análise que deseja executar:")
        print("1 - DadosBrasil")
        print("2 - PorcentagemMedalhas")
        print("3 - QuemTemMaisMedalhas")
        print("4 - Participação")
        print("5 - SemMedalhas")
        print("6 - CidadeSede")
        print("0 - Sair")

        choice = input("Digite o número da análise: ")

        if choice == '1':
            DadosBrasil.DadosBrasil(caminho_csv)
        elif choice == '2':
            PorcentagemMedalhas.PorcentagemMedalhas(caminho_csv)
        elif choice == '3':
            QuemTemMaisMedalhas.QuemTemMaisMedalhas(caminho_csv)
        elif choice == '4':
            Participacao.Participacao(caminho_csv)
        elif choice == '5':
            SemMedalhas.SemMedalhas(caminho_csv)
        elif choice == '6':
            CidadeSede.CidadeSede()
        elif choice == '0':
            print("Programa Encerrado!")
            break
        else:
            print("Escolha inválida. Por favor, digite um número válido.")

if __name__ == "__main__":
    main()