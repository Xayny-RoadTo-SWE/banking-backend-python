import mysql.connector
from mysql.connector import Error
import config  # importa as credenciais do config.py

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME
        )
        return conn
    except Error as e:
        print("Erro ao conectar no MySQL:", e)
        raise

def create_user(nome):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO users (nome, saldo) VALUES (%s, %s)"
        cursor.execute(sql, (nome, 0.00))

        conn.commit()
        print(f"Usuário '{nome}' criado com sucesso com saldo inicial de 0.00!")
    
    except Error as e:
        print("Erro ao criar usuário:", e)
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_user("Alex")
