from flask import request, jsonify
from app import app
from app import jwt
from usermodel import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

