from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InputForm(FlaskForm):
    new_task= StringField('Add new task')
    submit= SubmitField('submit')
