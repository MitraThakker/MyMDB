from flask import Flask, jsonify, request

from src.users import svc as user_svc

app = Flask('user')


@app.route('/', methods=['GET'])
def index():
    return "Hello, world!"


@app.route('/movies', methods=['GET'])
def list_all_movies():
    result = user_svc.list_all_movies()
    if result is not None:
        return jsonify(result), 200
    return "error", 500


@app.route('/movie/<int:movie_id>', methods=['GET'])
def movie_details(movie_id: int):
    result = user_svc.movie_details(movie_id)
    if result is not None:
        return jsonify(result), 200
    return "error", 500


@app.route('/movie/search', methods=['GET'])
def search_movie():
    search_string = request.args.get('query', '')
    result = user_svc.search_movie(search_string)
    if result is not None:
        return jsonify(result), 200
    return "error", 500


if __name__ == '__main__':
    app.run(debug=True, port=5002)
