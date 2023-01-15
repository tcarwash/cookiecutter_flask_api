import psycopg2
from time import sleep
import os, sys

DB_NAME = os.environ.get("POSTGRES_NAME")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")


def main():
    while True:
        try:
            conn = psycopg2.connect(
                f"host=db dbname={DB_NAME} password={DB_PASS} user={DB_PASS}"
            )
            conn.close()
            return 0
        except psycopg2.OperationalError as e:
            print("Database not yet ready")
            sleep(1)


if __name__ == "__main__":
    sys.exit(main())
