# Auth Forms: Log In and Sign Up

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignupForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")
    
class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log In")
    
class AddTaskForm(FlaskForm):
    title = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Task Title'})
    status = HiddenField('Task Status', validators=[DataRequired()], default="ToDo")
    submit = SubmitField('Add Task')