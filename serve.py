import http.server
import socketserver

# Сервер БЕЗ кеширования: браузер всегда получает свежую версию страницы.
# Из-за кеша раньше страница не видела новые правки, и казалось,
# что сохранение ленты "не работает".


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, *args):
        pass


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('', 8477), Handler) as httpd:
    httpd.serve_forever()
