import socket
import json

host = '0.0.0.0'
port = 8080

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

s.bind((host,port))

s.listen(5)

html = """
<!DOCTYPE html>
    <html>
    <head>
        <title>Python Socket Server</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                max-width: 800px; 
                margin: 50px auto; 
                padding: 20px;
                background-color: #f4f4f4;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 { color: #333; }
            .info { 
                background: #e7f3ff; 
                padding: 15px; 
                border-left: 4px solid #2196F3;
                margin: 20px 0;
            }
            .stats {
                display: flex;
                gap: 20px;
                margin: 20px 0;
            }
            .stat-box {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                text-align: center;
                flex: 1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Python Socket Server</h1>
            
            <div class="info">
                <strong>Server Status:</strong> Running successfully!<br>
                <strong>Protocol:</strong> HTTP over TCP<br>
                <strong>Port:</strong> 8080
            </div>
            
            <div class="stats">
                <div class="stat-box">
                    <h3>Server Info</h3>
                    <p>Built with Python sockets</p>
                </div>
                <div class="stat-box">
                    <h3>Connection</h3>
                    <p>Single client handling</p>
                </div>
                <div class="stat-box">
                    <h3>Features</h3>
                    <p>HTTP/1.1 compliant</p>
                </div>
            </div>
            
          <h2>Welcome!</h2>
          <p>This is a custom HTTP server built from scratch using</p>
            
            
        </div>
    </body>
    </html>

"""

response = f"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}

{html}"""

while True:
  csocket , caddr = s.accept()
  
  csocket.send(response.encode('utf-8'))
  
  # re = csocket.recv(1024).decode('utf-8')
  
  # target = re.split('\n')[0].split()[1]
  
  csocket.close()
  
  print(caddr[0])

s.close()

