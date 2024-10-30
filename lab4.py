from flask import Blueprint, url_for, redirect, render_template, request, make_response
lab3 = Blueprint('lab4', __name__)

@lab3.route('/lab4/')
def lab():
    return render_template('lab4/lab4/html')