from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField, IntegerField, StringField
from wtforms.validators import DataRequired
from wtforms.fields import EmailField


class WorksForm(FlaskForm):
    team_leader = IntegerField('Начальник работ', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField('Время работы', validators=[DataRequired()])
    collaboratos = StringField('участники работ', validators=[DataRequired()])
    is_finished = BooleanField('Закончена')
    submit = SubmitField('Добавить')
