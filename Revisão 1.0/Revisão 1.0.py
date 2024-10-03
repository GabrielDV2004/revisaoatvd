""""
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade,sexo(M,F) e sálario.
Faça um algoritmo que informe:

  A - a média de salario do grupo
  B - maior e menor idade do grupo
  C - quantidade de mulheres com salario a partir de R$5.000,00

Crie um menu com 3 opçôes.

Código | Descrição
1      | Adicionar pessoa
2      | Exibir resultados
3      | Sair
 
O final da leitura de dados se dará com quando o usuário digitar o número código 3

Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.
1. Salve os dados em um arquivo com nome: pesquisa_habitantes.txt
2. O programa deve ler o arquivo para exibir os dados salvos.

===Participantes===
1- Gabriel Pinto dos santos
2- Gabriel Neves
"""
import os 
os.system("cls || clear ")
from dataclasses import dataclass

dados_pesquisa = []
contador = 0

while True:
    print("O que você quer fazer?")
    print("1. Adicionar uma pessoa à pesquisa")
    print("2. Ver os resultados da pesquisa")
    print("3. Sair")

    opcao = int(input("Digite sua opção: "))

    # Se o usuário escolher a opção 1, vamos pedir as informações da pessoa
    if opcao == 1:
        contador += 1
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: "))
        #Apagamos os dados agora
        os.system("cls || clear ")

        # Adicionamos as informações da pessoa na lista
        dados_pesquisa.append((idade, sexo, salario))
        print("Pessoa adicionada com sucesso!")

        # Colocamos os dados dos habitantes no banco de dados, assim criamos um
        nome_arquivo = "pesquisa_habitantes.txt"
        with open(nome_arquivo, "a") as arquivo_habitantes:
            for i in range(1):
                arquivo_habitantes.write(f"Dados: idade {idade}, sexo {sexo}, salário {salario}\n")
        arquivo_habitantes.close()


    # Se o usuário escolher a opção 2, vamos calcular as estatísticas
    elif opcao == 2:
        # Inicializamos algumas variáveis para guardar os resultados
        if contador == 0:
            print("Não concluído, tente novamente.")
            break
        soma_salarios = 0
        maior_idade = 0
        menor_idade = 999  # Um número bem grande para garantir que a primeira idade será menor
        cont_mulheres_salario_alto = 0

        # Percorremos a lista de dados para fazer os cálculos
        for pessoa in dados_pesquisa:
            idade, sexo, salario = pessoa
            soma_salarios += salario
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            if sexo == 'F' and salario >= 5000:
                cont_mulheres_salario_alto += 1

        # Calculamos a média dos salários
        media_salarios = soma_salarios / len(dados_pesquisa)

        # Imprimimos os resultados
        print("Resultados da pesquisa:")
        print(f"Média salarial: R$ {media_salarios:.2f}")
        print(f"Maior idade: {maior_idade}")
        print(f"Menor idade: {menor_idade}")
        print(f"Quantidade de mulheres com salário acima de R$5000: {cont_mulheres_salario_alto}")

    # Se o usuário escolher a opção 3, saímos do programa
    elif opcao == 3:
        print("Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")