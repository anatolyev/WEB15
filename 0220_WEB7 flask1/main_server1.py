from http.server import HTTPServer, CGIHTTPRequestHandler

server_adress = ("", 8000)
httpd = HTTPServer(server_adress, CGIHTTPRequestHandler)
httpd.serve_forever()

# Для входа на сервер нужно ввести в браузере адрес:
# http://127.0.0.1:8000
