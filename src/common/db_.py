import logging
import sqlite3
from abc import ABC
from threading import local

logging.basicConfig(
    level=logging.INFO
)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


t_local = local()


class DBConnection(ABC):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class SQLiteDBConnection(DBConnection):
    def __init__(self):
        self.db = '/opt/db/movies.db'

    def __enter__(self):
        try:
            self.fresh_conn = False
            self.db_connection = getattr(t_local, '_conn', None)
            if self.db_connection is None:
                self.fresh_conn = True
                self.db_connection = sqlite3.connect(self.db)
                self.db_connection.row_factory = dict_factory
                setattr(t_local, '_conn', self.db_connection)
        except Exception as db_error:
            raise db_error
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fresh_conn:
            if exc_type is not None:
                self.db_connection.rollback()
                logging.error(f'{exc_type.__name__}: {exc_val}')
            else:
                self.db_connection.commit()
            self.db_connection.close()
            self.db_connection = None
            setattr(t_local, '_conn', self.db_connection)


def main():
    with SQLiteDBConnection() as conn:
        result = conn.execute('SELECT * FROM sqlite_master')
        for row in result.fetchall():
            print(row)


if __name__ == '__main__':
    main()
