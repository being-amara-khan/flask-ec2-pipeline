from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deployed by Amara Khan</title>
        <style>
            body {
                background-color: #f5f0ff;
                font-family: 'Segoe UI', sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                color: #6a1b9a;
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            p {
                color: #333;
                font-size: 1.2rem;
            }
            .tag {
                margin-top: 20px;
                background: #e1bee7;
                color: #4a148c;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Hello from Flask on EC2 via Azure DevOps!</h1>
        <p>This CI/CD pipeline was built with 💙, late-night coffee ☕, and 100% hustle by Amara Khan.</p>
        <div class="tag">#TechByAmara</div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
