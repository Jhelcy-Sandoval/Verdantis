from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

#formulario para obtener datos de las plantas
class PlantForm(FlaskForm):
    tag = StringField('Tag', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    germination_date = DateTimeField('Germination Date', validators=[DataRequired()])
    initial_conditions = StringField('Initial Conditions')
    submit = SubmitField('Register')
