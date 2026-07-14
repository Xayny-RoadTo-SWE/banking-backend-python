import psycopg2
from psycopg2 import Error as PostgresError
from psycopg2.extras import RealDictCursor
import config
import logging
from typing import Optional

def get_connection():
    try:
        return psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            dbname=config.DB_NAME
        )
    except PostgresError as e:
        print("Erro ao conectar no PostgreSQL:", e)
        raise

class DatabaseAdapter:
    @staticmethod
    def insert(query: str, *params) -> Optional[bool]:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(query, params if params else None)
            conn.commit()
            return True
        except PostgresError as e:
            logging.error(f"Error on inserting database: {e}")
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
            
            cursor.execute(query, args)
            return cursor.fetchone()
        
        except PostgresError as e:
            logging.error(f"Error on fetching data from database: {e}")
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
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute(query, args)
            result = cursor.fetchone()
            return result
        except PostgresError as e:
            logging.error(f"Error on fetching dict from database: {e}")
            raise
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()