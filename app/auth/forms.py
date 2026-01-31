from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('Ad', validators=[DataRequired()])
    last_name = StringField('Soyad', validators=[DataRequired()])
    email = StringField('E-posta', validators=[DataRequired(), Email()])
    phone = StringField('Telefon Numarası', validators=[DataRequired()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    accept_terms = BooleanField('Şartlar ve koşulları kabul ediyorum', validators=[DataRequired()])
    submit = SubmitField('Kayıt Ol')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Bu e-posta adresi zaten kullanımda.')

    def validate_phone(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('Bu telefon numarası zaten kullanımda.')

class LoginForm(FlaskForm):
    email = StringField('E-posta', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    remember_me = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')