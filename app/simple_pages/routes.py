from flask import Blueprint, render_template

bp = Blueprint('simple_pages', __name__)


@bp.get('/')
def home():
    return 'hey'
