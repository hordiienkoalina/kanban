from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Define the sign-up form
class SignupForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])  # Email input field
    password = PasswordField('Password', 
                            validators=[DataRequired()])  # Password input field
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])  # Confirm password input field
    submit = SubmitField("Sign Up")  # Submit button

# Define the login form
class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])  # Email input field
    password = PasswordField('Password', 
                            validators=[DataRequired()])  # Password input field
    remember = BooleanField('Remember Me')  # Remember me checkbox
    submit = SubmitField("Log In")  # Submit button

# Define the add task form
class AddTaskForm(FlaskForm):
    title = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Task Title'})  # Task title input field
    status = HiddenField('Task Status', validators=[DataRequired()], default="ToDo")  # Hidden field for task status
    submit = SubmitField('Add Task')  # Submit button