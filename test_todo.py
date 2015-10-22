import requests

#
# def post_object():
#     r = requests.post('http://localhost:8000/api/todos/', data={'title':'This is a test post'})
#     print(r.status_code)
#     print(r.text)
#
# post_object()
#
# def get_object():
#     r = requests.get('http://localhost:8000/api/todos/')
#     print(r.status_code)
#     print(r.text)
# get_object()
#
# def delete_object():
#     r = requests.delete('http://localhost:8000/api/todos/{}'.format(input('please enter the id of the entry to be deleted')))
#     print(r.status_code)
#     print(r.text)
#
# delete_object()
#
# def put_object():
#     r = requests.put('http://localhost:8000/api/todos/{}/'.format(input('please enter the id to change')),data={'title':'new_data'})
#     print(r.status_code)
#     print(r.text)
# put_object()

def test_post():
    r = requests.post('http://localhost:8000/api/todos/', data={'title':'This is a test post'})
    assert r.status_code == 201

def test_get():
    r = requests.get('http://localhost:8000/api/todos/')
    assert r.status_code == 200

def test_delete():
    num = requests.get('http://localhost:8000/api/todos/').json()[0]['id']
    r = requests.delete('http://localhost:8000/api/todos/{}'.format(num))
    assert r.status_code == 204

def test_put():
    num = requests.get('http://localhost:8000/api/todos/').json()[0]['id']
    r = requests.put('http://localhost:8000/api/todos/{}/'.format(num),data={'title':'something new'})
    print(r.json())
    assert r.status_code == 200
    assert r.json() == {'title': 'something new',
                        'id': int('{}'.format(num)),
                        'order': None,
                        'completed': False}
