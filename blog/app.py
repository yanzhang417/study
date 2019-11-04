from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from show_all import load_all_from_mysql
from show_id import load_one_from_mysql

app = Flask(__name__)
app.secret_key = 'dklsdfjsdjgklgjkdjglkf'

class MyForm(Form):  # 定义了表单的样子
    name = StringField('user-name:', validators=[DataRequired()])
    pwd = PasswordField('pwd:', validators=[DataRequired()])
    pwd2 = PasswordField('pwd2', validators=[DataRequired(), EqualTo('pwd')])
    submit = SubmitField('提交')

@app.route('/', methods=["GET", "POST"])
def hello_world():
    tuple = load_all_from_mysql()
    form = MyForm()
    if request.method == "GET":
        return render_template('log.html', form=form)
    else:
        if form.validate_on_submit():
            if request.form['name'] == 'abc' and request.form['pwd'] == '123':
                return render_template('0.html', content=tuple)
            return '参数正确'
        return 'a you ok'


@app.route('/blog/<int:id>')
def blog(id):
    print(id)
    tuple1 = load_one_from_mysql(id)
    print(tuple1)
    return render_template('03.html',row = tuple1)








@app.errorhandler(404)
def not_found(e):
    return '页面没找到', 404


if __name__ == '__main__':
    app.run()
