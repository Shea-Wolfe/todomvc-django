import requests


def post_object():
    requests.post('http://localhost:8000/api/todos/', data={'title':'This is a test post'})

post_object()

def delete_object():
    requests.delete('http://localhost:8000/api/todos/{}'.format(input('please enter the id of the entry to be deleted')))

delete_object()

def put_object():
    requests.put('http://localhost:8000/api/todos/{}/'.format(input('please enter the id to change')),data={'title':'new_data'})
put_object()
