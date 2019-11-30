import requests

url = "http://localhost:8000/hello/"

payload = """--d66f495a-c4d1-487c-9277-9ab1a20001cc
Content-Disposition: form-data; name=\"content\"
Content-Type: multipart/form-data; charset=utf-8

Hello World
--d66f495a-c4d1-487c-9277-9ab1a20001cc--"""

headers = {
    'Content-Type': "multipart/form-data; boundary=d66f495a-c4d1-487c-9277-9ab1a20001cc",
}

response = requests.request("POST", url, data=payload, headers=headers)

print('content: ', response.text, '\ncode: ', response.status_code)
