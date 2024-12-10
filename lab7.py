from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app
import sqlite3
import json
from os import path
import psycopg2
from psycopg2.extras import RealDictCursor
lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')