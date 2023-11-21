import fdb

# Conecte-se ao banco de dados Firebird
conn = fdb.connect(
    dsn='C:\ecosis\dados\Treinamento.eco',
    user='SYSDBA',
    password='masterkey',
    port=3050
)

# Crie um cursor para executar consultas SQL
cursor = conn.cursor()

try:
    # Execute uma consulta SQL para obter o dado que você deseja
    cursor.execute("Select km from tvenpedido where codigo = '0000626'")

    # Recupere o valor da consulta
    valor_temporario = cursor.fetchone()[0]

    # Faça alguma manipulação com o valor, se necessário
    novo_valor = valor_temporario + 22

    # Atualize o campo de destino na mesma tabela
    cursor.execute("Update tvenpedido set km = ? where codigo = '0000626'", (novo_valor,))

    # Commit (confirme) as alterações no banco de dados
    conn.commit()


except Exception as e:
    # Em caso de erro, faça um rollback (desfaça as alterações)
    conn.rollback()
    print(f"Erro: {e}")

finally:
    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()
