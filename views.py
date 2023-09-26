from flask import Blueprint
from models import User
from database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello, Cube-API!'
