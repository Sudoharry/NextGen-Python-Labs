# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, TextAreaField, validators
from flask_wtf import FlaskForm
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///h2m.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# Database Models
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False)

class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Forms
class ContactForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=2, max=100)])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    phone = StringField('Phone')
    message = TextAreaField('Message', [validators.DataRequired(), validators.Length(min=10)])

# Create database tables
with app.app_context():
    db.create_all()

# Error Handlers
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

# Routes
@app.route('/')
def home():
    print("Home route hit")
    services = Service.query.limit(4).all()
    projects = Portfolio.query.limit(3).all()
    return render_template('index.html', 
                         services=services,
                         projects=projects,
                         meta_description="H2M IT Solutions - Your digital transformation partner")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        submission = ContactSubmission(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            message=form.message.data
        )
        db.session.add(submission)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('contact.html', form=form)

@app.route("/services",methods=['GET','POST'])
def services():
    return render_template('services.html')


# @app.route('/blog',methods=['GET'])
# def blog():
#     return render_template('blog.html')


@app.route('/about-us' , methods=['GET', 'POST'])

def about_us():
    print("Home route hit")
    return render_template('about-us.html')


@app.route("/testimonials", methods=['GET', 'POST'])
def testimonials():
    return render_template('testimonials.html')

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html')


@app.route('/features', methods=['GET', 'POST'])
def features():
    return render_template('features.html')

@app.route('/pricing', methods=['GET', 'POST'])
def pricing():
    return render_template('pricing.html')

@app.route('/thank_you', methods=['GET', 'POST'])
def thank_you():
    return render_template('thank_you.html')

# ... other routes ...

if __name__ == '__main__':
    app.run(debug=True, port=8000)