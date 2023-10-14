from flask import Flask, render_template, redirect, url_for, flash, request, get_flashed_messages
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'secret_key_here'


class NumberForm(FlaskForm):
    number = IntegerField('Enter a positive integer:',
                          validators=[DataRequired()])
    submit = SubmitField('Check')


def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        num = form.number.data
        if is_fibonacci(num):
            flash('The number is in the Fibonacci series!', 'success')
            image_name = 'images/yes.png'
        else:
            flash('The number is not in the Fibonacci series.', 'danger')
            image_name = 'images/no.png'
        return redirect(url_for('result', image_name=image_name))
    return render_template('index.html', form=form)


@app.route('/result')
def result():
    image_name = request.args.get('image_name')
    messages = get_flashed_messages(with_categories=True)
    return render_template('result.html', messages=messages, image_name=image_name)


if __name__ == '__main__':
    app.run(debug=True)
