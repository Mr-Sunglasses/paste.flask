from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Add_Data(FlaskForm):

    data_paste = TextAreaField(label="Please Enter the Details to Paste", validators=[DataRequired()])
    submit = SubmitField(label="Paste")