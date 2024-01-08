from funcoes import conectar_banco, cadastrar_tipo_lancamento, incluir_lancamento, excluir_lancamento, consultar_lancamento, fechar_conexao

def menu():
    print("==== Sistema de Controle de Despesas ====")
    print("1. Cadastrar Tipo Lançamento")
    print("2. Incluir Lançamento")
    print("3. Excluir Lançamento")
    print("4. Consultar Lançamento")
    print("5. Sair")

def main():
    conexao = conectar_banco()

    if conexao:
        while True:
            menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                cadastrar_tipo_lancamento(conexao, descricao)
            elif opcao == "2":
                incluir_lancamento(conexao)
            elif opcao == "3":
                id_despesa = int(input("Digite o ID da despesa a ser excluída: "))
                excluir_lancamento(conexao, id_despesa)
            elif opcao == "4":
                consultar_lancamento(conexao)
            elif opcao == "5":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        fechar_conexao(conexao)

if __name__ == "__main__":
    main()