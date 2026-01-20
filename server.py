from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import os
import urllib.parse

STUDENT_NAME = "Шорохов Илья Александрович"
GROUP = "11.1-РПО-23.1-72"
SUBJECT = "Облачные технологии и использование Microsoft Azure при разработке приложений"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path

        if path == '/':
            server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Я сделяль</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: rgb(32, 32, 32);
            color: rgb(255,117,20);
            font-family: 'Roboto', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }}
        h1, h2, #time {{
            margin: 10px 0;
        }}
        #time {{
            font-size: 1.5em;
            font-weight: 700;
        }}
    </style>
</head>
<body>
    <h1>{STUDENT_NAME}, группа {GROUP}</h1>
    <h2>{SUBJECT}</h2>
    <div id="time">{server_time}</div>

    <script>
        // Получаем время сервера при загрузке
        const serverTimeStr = "{server_time}";
        const serverTime = new Date(serverTimeStr).getTime();
        const startTime = Date.now();
        const timeOffset = serverTime - startTime;

        function updateClock() {{
            const now = Date.now() + timeOffset;
            const date = new Date(now);
            const formatted = date.getFullYear() + '-' +
                String(date.getMonth() + 1).padStart(2, '0') + '-' +
                String(date.getDate()).padStart(2, '0') + ' ' +
                String(date.getHours()).padStart(2, '0') + ':' +
                String(date.getMinutes()).padStart(2, '0') + ':' +
                String(date.getSeconds()).padStart(2, '0');
            document.getElementById('time').textContent = formatted;
        }}

        updateClock();
        setInterval(updateClock, 1000);
    </script>
</body>
</html>
            """
            self.wfile.write(html.encode('utf-8'))

        elif path == '/time':
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1 style='color:rgb(255,117,20);background:rgb(32,32,32);font-family:Roboto'>404 — Страница не найдена</h1>".encode('utf-8'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    print(f"Сервер запущен на порту {port}")
    server.serve_forever()