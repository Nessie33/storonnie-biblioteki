import requests

sayt = 'https://jsonplaceholder.typicode.com/posts'
a = requests.get(sayt)
if a.status_code == 200:
    print('Данные получены')
    print(a.json())
else:
    print(f'Ошибка {a.status_code}: не удалось получить данные.')