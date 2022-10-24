from time import sleep
import requests

urls = ['http://127.0.0.1:8000/blog/',
        'http://127.0.0.1:8000/blog/about/',
        'http://127.0.0.1:8000/blog/error/',
        'http://127.0.0.1:8000/blog/error4/'
    ]

while True:
    try:
        
        
        for url in urls:
            sleep(5)
            print(requests.get(url=url).text)
    except Exception as e:
        print(e.__class__)

        