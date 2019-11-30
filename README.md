### Django Channels Bad Request
> A minimal reproduction of a channels bug on Python3.7+

#### Bug

For multipart requests, channels works flawlessly on Python 3.6.9 or older, but returns `400 Bad Request` on Python 3.7.0+  
The request does not even reach the views or middleware. This happens on the development server of channels run using `runserver`

Tested on Python 3.6.6, 3.6.9, 3.7.0, 3.7.4, 3.7.5, and 3.8.0. And as mentioned above, it's reproducible on all Python 3.7.0+ versions

#### Steps to reproduce

1. python3.6 -m .venv3.6
2. source .venv3.6/bin/activate
3. pip install -r requirements.txt
4. python manage.py runserver
5. python test.py
6. You should see `Hello World` as content and `200` OK as status code
7. Repeat steps 1 - 5 for `python3.7` or any version above, and you should see empty response content and `400` bad request as status code
