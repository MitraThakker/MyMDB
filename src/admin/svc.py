from src.admin import repo


def valid_movie_json(movie_json: dict) -> bool:
    if movie_json.get('name', '') and movie_json.get('director', ''):
        return True
    return False


def add_movie(movie_json: dict):
    if valid_movie_json(movie_json):
        try:
            return repo.add_movie(movie_json)
        except Exception:
            return False
    return False


def update_movie(movie_id: int, movie_json: dict):
    if valid_movie_json(movie_json):
        try:
            repo.update_movie(movie_id, movie_json)
            return True
        except Exception:
            return False
    return False


def delete_movie(movie_id: int):
    try:
        repo.delete_movie(movie_id)
        return True
    except Exception:
        return False
