import requests


def post_object():
    requests.post('http://localhost:8000/api/todos/', data={'title':'This is a test post'})

post_object()
