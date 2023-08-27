#подключаем модули и файлы, чтобы создать локальный сервер
from http.server import HTTPServer, CGIHTTPRequestHandler #первый создаёт локальный сервер. второй следит за переходом пользователя на главную страницу сайта

def server():
    server_data = ("localhost", 8000)
    server = HTTPServer(server_data, CGIHTTPRequestHandler)
    print("Server started")
    #чтобы локальный сервер работал и сайт мог обрабатываться
    server.serve_forever()

if __name__ == "__main__":
    server()