from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

# db rules creation

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)

	def __repr__(self):
		return '<User %r>' % self.name

	products = db.relationship('Product')


class Produts(db.Model):
	__tablename__ = "products"	
	id = db.Column(db.Integer, primary_key=True)
	productName = db.Column(db.String(64))
	productValue = db.Column(db.Numeric(2))

	user_id = db.Column(db.Integer, db.ForeignKey(users.id))


# creating tables

db.create_all()

myUser = User(1, 'john')
myFirstProduct = Produts(1, 'beer', 10.05)
