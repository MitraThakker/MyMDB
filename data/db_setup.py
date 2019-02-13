import json

from src.common.db_ import SQLiteDBConnection


def create_movies_table():
    with SQLiteDBConnection() as conn:
        conn.execute('''CREATE TABLE movies
                        (id INTEGER PRIMARY KEY,
                         name TEXT,
                         director TEXT,
                         imdb_score REAL,
                         popularity REAL)''')


def create_movie_genre_table():
    with SQLiteDBConnection() as conn:
        conn.execute('''CREATE TABLE movie_genre
                        (movie_id INTEGER,
                         genre TEXT,
                         FOREIGN KEY(movie_id) REFERENCES movies(id))''')


def populate_tables():
    with open('./imdb.json') as fp:
        movies_json = json.loads(fp.read())

    with SQLiteDBConnection() as conn:
        for movie in movies_json:
            cursor = conn.cursor()
            cursor.execute(f'''INSERT INTO movies VALUES
                                (NULL,
                                 "{movie.get("name", "")}",
                                 "{movie.get("director", "")}",
                                 {movie.get("imdb_score", 0.0)},
                                 {movie.get("popularity", 0.0)})''')
            movie_id = cursor.lastrowid
            for genre in movie.get("genre", []):
                cursor.execute(f'''INSERT INTO movie_genre VALUES
                                    ({movie_id},
                                     "{genre}")''')
            cursor.close()


if __name__ == '__main__':
    create_movies_table()
    create_movie_genre_table()
    populate_tables()
