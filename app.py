from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# Define templates for different languages
templates = {
    'html': "<!DOCTYPE html>\n<html>\n<head>\n<title>{{ title }}</title>\n</head>\n<body>\n<h1>Hello, World!</h1>\n</body>\n</html>",
    'css': "body {\n    font-family: Arial, sans-serif;\n}",
    'js': "document.addEventListener('DOMContentLoaded', function() {\n    console.log('Hello, World!');\n});",
    'python': "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    title = request.form.get('title')
    selected_langs = request.form.getlist('languages')

    generated_files = {}
    for lang in selected_langs:
        generated_files[lang] = templates.get(lang, '')

    return render_template('result.html', title=title, files=generated_files)

@app.route('/download/<lang>', methods=['GET'])
def download(lang):
    content = templates.get(lang, '')
    filename = f'template.{lang}'
    
    with open(filename, 'w') as f:
        f.write(content)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
