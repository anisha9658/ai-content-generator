# app/routes.py
from flask import Blueprint, render_template, request
from models.generate_text import generate_text

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['GET', 'POST'])
def generate():
    result = None
    if request.method == 'POST':
        title = request.form['title']
        content_type = request.form['content_type']
        genre = request.form['genre']
        style = request.form['style']
        audience = request.form.get('audience', '')

        result = generate_text(title, content_type, genre, style, audience)
    return render_template('generate.html', result=result)

@main.route('/history')
def history():
    # Placeholder until DB is added
    return render_template('history.html')

@main.route('/about')
def about():
    return render_template('about.html')
