from flask import Flask, jsonify, request, Response

from src.admin import svc as admin_svc
from src.users import svc as user_svc

app = Flask('admin')


@app.route('/', methods=['GET'])
def index():
    return "Hello, world!"


@app.route('/movies', methods=['GET'])
def list_all_movies():
    try:
        return jsonify(user_svc.list_all_movies())
    except Exception:
        return Response("error", status=503)


@app.route('/movie/<int:movie_id>', methods=['GET'])
def movie_details(movie_id: int):
    try:
        return jsonify(user_svc.movie_details(movie_id)), 200
    except Exception:
        return Response("error", status=500)


@app.route('/movie/search', methods=['GET'])
def search_movie():
    try:
        search_string = request.args.get('query', '')
        return jsonify(user_svc.search_movie(search_string)), 200
    except Exception:
        return Response("error", status=500)


@app.route('/movie/add', methods=['POST'])
def add_movie():
    req = request.get_json()
    movie_id = admin_svc.add_movie(req)
    if movie_id:
        return jsonify(movie_id), 200
    return Response("error", status=400)


@app.route('/movie/<int:movie_id>/update', methods=['PUT'])
def update_movie(movie_id: int):
    req = request.get_json()
    if admin_svc.update_movie(movie_id, req):
        return Response("success", status=200)
    else:
        return Response("error", status=400)


@app.route('/movie/<int:movie_id>/delete', methods=['DELETE'])
def delete_movie(movie_id: int):
    if admin_svc.delete_movie(movie_id):
        return Response("success", status=200)
    else:
        return Response("error", status=400)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
