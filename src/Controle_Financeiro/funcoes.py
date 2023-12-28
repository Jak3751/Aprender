import fdb

def conectar_banco():
    try:
        conexao = fdb.connect(
            dsn='C:\\Users\\jakson.silva\\Desktop\\Python\\Financeiro.fdb',
            user='SYSDBA',
            password='masterkey',
            port='3050',
            charset='UTF8'
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def cadastrar_despesa(conexao, descricao, valor):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO despesas (id, descricao, valor) VALUES (next value for despesas, ?, ?)", (descricao, valor))
        conexao.commit()
        print("Despesa cadastrada com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar despesa: {e}")

def lancar_despesa(conexao):
    descricao = input("Digite a descrição da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    cadastrar_despesa(conexao, descricao, valor)

def excluir_despesa(conexao, id_despesa):
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM despesas WHERE id = ?", (id_despesa,))
        conexao.commit()
        print("Despesa excluída com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir despesa: {e}")

def consultar_despesas(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM despesas")
        despesas = cursor.fetchall()
        for despesa in despesas:
            print(f"ID: {despesa[0]}, Descrição: {despesa[1]}, Valor: {despesa[2]}")
    except Exception as e:
        print(f"Erro ao consultar despesas: {e}")

def fechar_conexao(conexao):
    try:
        conexao.close()
    except Exception as e:
        print(f"Erro ao fechar a conexão: {e}")