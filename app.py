from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from processing import get_similar

DEBUG = True
app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret'

class MyForm(FlaskForm):
    book = StringField('Book name:', validators=[DataRequired()])
    submit = SubmitField('Recommend me a book')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend", methods=['GET', 'POST'])
def recommend():
    form = MyForm()

    if request.method == 'POST':
        res = get_similar(form.book.data)
        if len(res['Author books']) > 0:
            for book in res['Author books']:
                flash(book, 'author')
        else:
            flash("Sorry, there are no corresponding books", 'no_book')
        
        if len(res['Year books']) > 0:
            for book in res['Year books']:
                flash(book, 'year')
        
    return render_template('recommend.html', form=form)

if __name__ == "__main__":
    app.run(port=5000)
    app.debug = DEBUG