import urllib.request

with urllib.request.urlopen('http://127.0.0.1:8000/index.html') as f:
    print(f.read(300))