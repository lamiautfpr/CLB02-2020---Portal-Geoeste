from flask import Blueprint, render_template
from jinja2 import TemplateNotFound


bp = Blueprint('portalgeoeste', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')
    