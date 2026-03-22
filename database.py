import pymysql
import config
import logging
from typing import Optional

def get_connection():
    try:
        return pymysql.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            autocommit=False
        )
    except MySQLError as e:
        print("Erro ao conectar no MySQL:", e)
        raise

class DatabaseAdapter:
    @staticmethod
    def insert(query: str, *params) -> Optional[bool]:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(query, *params)
            conn.commit()
            return True
        except MySQLError as e:
            logging.info("Error on inserting database", e)
            raise
        finally:
            if "cursor" in locals() and cursor:
                cursor.close()
            if "conn" in locals() and conn:
                conn.close()


    @staticmethod
    def fetchone(query: str, *args):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            return cursor.execute(query, *args).fetchone()
            
        except MySQLError as e:
            logging.info("Error on fetching data from database", e)
            raise
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()
    
    @staticmethod
    def fetchdict(query: str, *args):
        try:
            conn = get_connection()
            cursor = conn.cursor(psycopg2.cursors.DictCursor)
            cursor.execute(query, *args)
            result = cursor.fetchone()
            return result
        except MySQLError as e:
            logging.info("Error on fetching dict from database", e)
            raise
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()