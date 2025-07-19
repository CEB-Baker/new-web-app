from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
        <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background-color: #f4f4f9;
                    }
                    .outer-container {
                        border: 5px solid blue;
                        padding: 10px;
                        border-radius: 15px;
                    }
                    .welcome-container {
                        text-align: center;
                        border: 2px solid #ccc;
                        padding: 20px;
                        border-radius: 10px;
                        background-color: #fff;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }
                    h1 {
                        color: #333;
                    }
                </style>
            </head>
            <body>
                <div class="outer-container">
                    <div class="welcome-container">
                        <h1>Welcome to the New Web App!</h1>
                        <p>This is an AI company dedicated to innovation and technology.</p>
                    </div>
                </div>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50431)