from flask import Blueprint

logIn = Blueprint('logIn', __name__)

@admin.route('/logIn')
def logIn():
    return 'logIn Page'