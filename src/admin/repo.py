from src.common.db_ import SQLiteDBConnection


def add_movie(movie_json: dict):
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO movies VALUES
                           (NULL,
                            "{movie_json.get("name", "")}",
                            "{movie_json.get("director", "")}",
                            {movie_json.get("imdb_score", 0.0)},
                            {movie_json.get("popularity", 0.0)})''')

        movie_id = cursor.lastrowid
        for genre in movie_json.get("genres", []):
            cursor.execute(f'''INSERT INTO movie_genre VALUES
                               ({movie_id},
                                "{genre}"''')
        cursor.close()
    return movie_id


def update_movie(movie_id: int, movie_json: dict):
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''UPDATE movies SET
                                name="{movie_json.get("name", "")}",
                                director="{movie_json.get("director", "")}",
                                imdb_score={movie_json.get("imdb_score", 0.0)},
                                popularity={movie_json.get("popularity", 0.0)}
                           WHERE id={movie_id}''')
        cursor.execute(f'''DELETE FROM movie_genre WHERE movie_id={movie_id}''')
        for genre in movie_json.get("genres", []):
            cursor.execute(f'''INSERT INTO movie_genre VALUES
                               ({movie_id},
                                "{genre}")''')
        cursor.close()


def delete_movie(movie_id: int):
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''DELETE FROM movies
                           WHERE id={movie_id}''')
        cursor.execute(f'''DELETE FROM movie_genre WHERE movie_id={movie_id}''')
        cursor.close()
