import pymysql
from pymysql import MySQLError
import app.config as config
import logging
from typing import Optional

def get_connection():
    try:
        return psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            cursor_factory=RealDictCursor
        )
    except psycopg2.Error as e:
        print("Erro ao conectar no PostgreSQL:", e)
        raise

class DatabaseAdapter:
    @staticmethod
    def insert(query: str, *params) -> Optional[bool]:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(query, params)
            conn.commit()
            return True
        except psycopg2.Error as e:
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
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query, *args)
            result = cursor.fetchone()
            return result
        except psycopg2.Error as e:
            logging.info("Error on fetching data from database: %s", e)
            raise
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()
    
    @staticmethod
    def fetchdict(query: str, *args):
        return DatabaseAdapter.fetchone(query, *args)
    
    @staticmethod
    def fetchalldict(query: str, *args):
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query, *args)
            result = cursor.fetchall()
            return result
        except psycopg2.Error as e:
            logging.info("Error on fetching all data from database: %s", e)
            raise
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()