import requests

path = 'test/assets/buckettest.jpg'

resp = requests.post("https://trashify-tklllz773q-et.a.run.app",
                     files={'file': open(path, 'rb')})

print(resp.json())
