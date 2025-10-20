import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

class SPATestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # 处理SPA的路由请求
        if self.path.startswith('/sections/'):
            section_num = self.path.split('/')[-1]
            # 提供英文内容，避免编码问题
            texts = [
                '<h2>Section 1 Content</h2><p>This is the detailed content of section 1, loaded asynchronously via AJAX.</p><p>Single Page Application can update this content without refreshing the entire page.</p>',
                '<h2>Section 2 Content</h2><p>This is the detailed content of section 2, demonstrating the dynamic loading feature of SPA.</p><p>Click different buttons to switch and display different content.</p>',
                '<h2>Section 3 Content</h2><p>This is the detailed content of section 3, showing the interaction method of front-end and back-end separation.</p><p>The browser\'s back and forward buttons also work normally.</p>'
            ]
            if section_num.isdigit() and 1 <= int(section_num) <= 3:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(texts[int(section_num) - 1].encode('utf-8'))
                return
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<span style="color: red;">Section does not exist</span>'.encode('utf-8'))
                return
        
        # 处理section1、section2、section3路径（历史记录功能）
        elif self.path.startswith('/section'):
            # 提供index.html，但不改变URL
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                with open('spa_app/templates/spa_app/index.html', 'rb') as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.wfile.write('<h1>404 Not Found</h1>'.encode('utf-8'))
            return
        
        # 根路径请求index.html
        elif self.path == '/':
            self.path = '/spa_app/templates/spa_app/index.html'
            try:
                super().do_GET()
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<h1>404 Not Found</h1>'.encode('utf-8'))
        else:
            # 其他路径返回404
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<h1>404 Not Found</h1>'.encode('utf-8'))
            
    # 自定义日志输出，减少不必要的信息
    def log_message(self, format, *args):
        return

# 启动测试服务器
def run_server():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SPATestHandler)
    
    print(f"\nSPA测试服务器启动成功！")
    print(f"服务器运行在 http://localhost:{port}/")
    print("按 Ctrl+C 停止服务器")
    
    # 自动打开浏览器
    webbrowser.open(f'http://localhost:{port}/')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.server_close()

if __name__ == '__main__':
    run_server()