import time

def app(environ, start_response):
  data = b"Hello, World!\n"

  time.sleep(2)

  start_response("200 OK", [
    ("Content-Type", "text/plain"),
    ("Content-Length", str(len(data)))
  ])
  return iter([data])
