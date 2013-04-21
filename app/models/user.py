from app import db
from .bbs import Bbs_post, Bbs_cmt

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	urlname = db.Column(db.String(10), unique=True)
	nickname = db.Column(db.String(10), unique=True)
	anonyname = db.Column(db.String(10), unique=True)
	reg_time = db.Column(db.DateTime)
	last_login = db.Column(db.DateTime)
	seen = db.Column(db.SmallInteger, default=1)
	status = db.Column(db.SmallInteger, default=1)

	bbs_post = db.relationship('Bbs_post', backref='author', lazy='dynamic')
	bbs_cmt = db.relationship('Bbs_cmt', backref='author', lazy='dynamic')

	def __init__(self):
		pass

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.nickname)