from myapp import app
from model import User, Vehicle
from flask import request
from flask import jsonify
import flask_bcrypt
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime
from datetime import timedelta
from functools import wraps




def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
			print("token found in req------------", token)
		if not token:
			return jsonify({'message' : 'Token is missing!'})
		try:
			decoded_token = jwt.decode(token + "==", 'secret', algorithms=['HS256'], verify=False)
		except:
			return jsonify({'message' : 'Token is invalid!'})
		return f(decoded_token, *args, **kwargs)
	return decorated



class Login():
	@app.route('/userlogin/', methods = ['POST'])
	def post():
		json_data = request.get_json(force=True)
		email = json_data['email']
		password = json_data['password']
		username = json_data['username']
		print(email)

		result = User.query.filter(username == username)

		if not result:
			return jsonify({'message' : "user was not found"})
		if result:
			response = {}
			for index, res in enumerate(result):
				response[index] = {
	            "id": res.id,
	            "username": res.username,
	            "email_id": res.email_id,
	            "password": res.password,
	            "access_level": res.access_level,
	            "flag": res.flag
	            }
			db_password = response[0]['password']
			db_username = response[0]['username']
			db_access_level = response[0]['access_level']
			password_verf = flask_bcrypt.check_password_hash(db_password, password)
			if password_verf == True  :
				del db_password
				data = {'username' : db_username, 'access_level': db_access_level, 'exp' : datetime.utcnow() + timedelta(minutes=30)}
				token = jwt.encode(data, 'secret', 'HS256').decode('utf-8')
				decoded = jwt.decode(token, 'secret', algorithms=['HS256'], verify=False)
				print("token found------------", decoded)
				
				return jsonify({'token' : token})
			else:
				return jsonify({'message': 'wrong password'})


class Register():
	@app.route('/registeruser/', methods = ['POST'])
	@token_required
	def registerpost(decoded_token):
		current_user = decoded_token
		print("current_user----------",current_user)
		return jsonify({'status': 'ok'})
