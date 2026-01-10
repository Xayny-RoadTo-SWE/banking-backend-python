import pymysql
from pymysql import MySQLError
import config


def get_connection():
    try:
        return pymysql.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME,
            autocommit=False
        )
    except MySQLError as e:
        print("Erro ao conectar no MySQL:", e)
        raise


def create_user(nome):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (nome, saldo) VALUES (%s, %s)",
            (nome, 0.00)
        )

        conn.commit()
        print(f"Usuário '{nome}' criado com sucesso!")

    except MySQLError as e:
        print("Erro ao criar usuário:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def get_balance(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT saldo FROM users WHERE id = %s",
            (user_id,)
        )

        result = cursor.fetchone()

        if result is None:
            print("Usuário não encontrado.")
            return None

        return result[0]

    except MySQLError as e:
        print("Erro ao consultar saldo:", e)
        return None

    finally:
        cursor.close()
        conn.close()


def deposit(user_id, amount):
    if amount <= 0:
        print("Valor inválido.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET saldo = saldo + %s WHERE id = %s",
            (amount, user_id)
        )

        if cursor.rowcount == 0:
            print("Usuário não encontrado.")
            conn.rollback()
            return

        conn.commit()
        print(f"Depósito de {amount:.2f} realizado com sucesso!")

    except MySQLError as e:
        print("Erro no depósito:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def withdraw(user_id, amount):
    if amount <= 0:
        print("Valor inválido.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT saldo FROM users WHERE id = %s",
            (user_id,)
        )

        result = cursor.fetchone()

        if result is None:
            print("Usuário não encontrado.")
            return

        saldo = result[0]

        if saldo < amount:
            print("Saldo insuficiente.")
            return

        cursor.execute(
            "UPDATE users SET saldo = saldo - %s WHERE id = %s",
            (amount, user_id)
        )

        conn.commit()
        print(f"Saque de {amount:.2f} realizado com sucesso!")

    except MySQLError as e:
        print("Erro no saque:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def transfer(from_user_id, to_user_id, amount):
    if amount <= 0 or from_user_id == to_user_id:
        print("Transferência inválida.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT saldo FROM users WHERE id = %s FOR UPDATE",
            (from_user_id,)
        )

        from_result = cursor.fetchone()

        if from_result is None or from_result[0] < amount:
            print("Saldo insuficiente ou usuário inválido.")
            conn.rollback()
            return

        cursor.execute(
            "SELECT id FROM users WHERE id = %s",
            (to_user_id,)
        )

        if cursor.fetchone() is None:
            print("Usuário destino não encontrado.")
            conn.rollback()
            return

        cursor.execute(
            "UPDATE users SET saldo = saldo - %s WHERE id = %s",
            (amount, from_user_id)
        )

        cursor.execute(
            "UPDATE users SET saldo = saldo + %s WHERE id = %s",
            (amount, to_user_id)
        )

        conn.commit()
        print(
            f"Transferência de {amount:.2f} "
            f"de usuário {from_user_id} para {to_user_id} realizada!"
        )

    except MySQLError as e:
        print("Erro na transferência:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def main():
    while True:
        print("\n===== BANCO EBANX =====")
        print("1 - Criar usuário")
        print("2 - Consultar saldo")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Transferir")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            create_user(input("Nome: "))

        elif opcao == "2":
            saldo = get_balance(int(input("ID: ")))
            if saldo is not None:
                print(f"Saldo: {saldo:.2f}")

        elif opcao == "3":
            deposit(
                int(input("ID: ")),
                float(input("Valor: "))
            )

        elif opcao == "4":
            withdraw(
                int(input("ID: ")),
                float(input("Valor: "))
            )

        elif opcao == "5":
            transfer(
                int(input("Remetente: ")),
                int(input("Destino: ")),
                float(input("Valor: "))
            )

        elif opcao == "0":
            print("Encerrando.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
