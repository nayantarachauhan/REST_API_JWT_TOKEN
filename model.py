from myapp import db
class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(100))
	email_id= db.Column(db.String(50), unique=True)
	password = db.Column(db.String(100))
	access_level = db.Column(db.String(100))
	flag = db.Column(db.String(100))

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ref_num = db.Column(db.String(80))
    make = db.Column(db.String(50), unique=True)
    model = db.Column(db.String(50))
    score = db.Column(db.String(80))
    result = db.Column(db.String(80))
    num_plate = db.Column(db.String(80))
    comment = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime(80))
    updated_at  = db.Column(db.DateTime(80))
    source_name = db.Column(db.String(80))
    claim_state = db.Column(db.String(5))
    user_id = db.Column(db.String(80))
    image_count = db.Column(db.Integer)
    reviewer_comment = db.Column(db.String(80))

