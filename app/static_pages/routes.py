from flask import Blueprint, render_template

bp = Blueprint('static_pages', __name__)


@bp.get('/')
def home():
    return 'hey'
