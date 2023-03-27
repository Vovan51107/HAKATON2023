from flask import Flask
from flask import request
from flask import redirect
from flask import render_template_string

from parser import Parser


server = Flask(__name__)

site_url = '10.243.64.63:5000'

def page(html_path, style_path):
    return set_style(render(html_path), 'static/style.css')

def render(html_path):
    with open(html_path) as file:
        return file.read()

def set_style(html, style_path):
    with open(style_path) as file:
        style = file.read()
        html = f'<head><style>{style}</head></style>{html}'
    return html

@server.route('/')
def index_page():
    return redirect('glavnaya.html')

@server.route('/glavnaya.html')
def main_page():
    return page('template/glavnaya.html', 'static/style.css')

@server.route('/zaglushka.html')
def zagl_page():
    return page('template/zaglushka.html', 'static/style.css')

@server.route('/posik.html')
def poisk_page():
    return page('template/poisk.html', 'static/style.css')

@server.route('/get_course')
def get_course():
    lst = Parser().parse('')
    txt = page('template/list.html', 'static/style.css')
    txt = txt.replace('rrr', lst)
    return txt
