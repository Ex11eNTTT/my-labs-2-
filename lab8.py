from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app, jsonify
import sqlite3
import json
from os import path
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def main_l8():
    return render_template('lab8/lab8.html')