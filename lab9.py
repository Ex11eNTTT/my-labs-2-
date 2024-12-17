from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app, jsonify
import sqlite3
import json
from os import path
from db import db
from db.models import users, articles
from datetime import datetime
import psycopg2
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from psycopg2.extras import RealDictCursor
lab9 = Blueprint('lab9', __name__)