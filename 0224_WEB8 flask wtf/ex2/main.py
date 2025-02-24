from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = "kjfqwe23093c.zfa'ewfl2"


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('index.html', username="Доступ открыт!")


if __name__ == '__main__':
    print('http://127.0.0.1:8080/login')
    app.run(port=8080, host='127.0.0.1')