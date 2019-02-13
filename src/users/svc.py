from src.users import repo


def list_all_movies():
    try:
        return repo.list_all_movies()
    except Exception:
        return None


def movie_details(movie_id: int):
    try:
        return repo.movie_details(movie_id)
    except Exception:
        return None


def search_movie(search_string: str):
    search_string = search_string.strip()
    try:
        if not search_string:
            return repo.list_all_movies()
        return repo.search_movie(search_string)
    except Exception:
        return None
