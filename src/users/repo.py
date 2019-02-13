from src.common.db_ import SQLiteDBConnection


def list_all_movies():
    with SQLiteDBConnection() as conn:
        result = conn.execute('''SELECT * FROM movies''')
        movies = result.fetchall()
    return movies


def movie_details(movie_id: int):
    with SQLiteDBConnection() as conn:
        result = conn.execute(f'''SELECT * FROM movies WHERE id={movie_id}''')
        movie = result.fetchone()
        result = conn.execute(f'''SELECT genre FROM movie_genre WHERE movie_id={movie_id}''')
        movie['genres'] = [genre.get('genre', '') for genre in result.fetchall()]
    return movie


def search_movie(search_string: str):
    with SQLiteDBConnection() as conn:
        result = conn.execute(f'''SELECT * FROM movies
                                   WHERE name LIKE "%{search_string}%"
                                   COLLATE NOCASE''')
        result_by_name = result.fetchall()

        result = conn.execute(f'''SELECT * FROM movies
                                   WHERE director LIKE "%{search_string}%"
                                   COLLATE NOCASE''')
        result_by_director = result.fetchall()
    return result_by_name + result_by_director
