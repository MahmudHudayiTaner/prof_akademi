from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from sqlalchemy.exc import IntegrityError

from app.auth.forms import RegistrationForm, LoginForm
from app.models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Yeni kullanıcı nesnesi oluşturma
        user = User(
            email=form.email.data,
            phone=form.phone.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        # Şifreyi hashleyerek set etme
        user.set_password(form.password.data)
        
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Bu e-posta adresi (veya telefon numarası) ile daha önce kayıt olunmuş.', 'danger')
            return render_template('auth/register.html', title='Kayıt Ol', form=form)

        flash('Tebrikler, başarıyla kayıt oldunuz!', 'success')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        for field_errors in form.errors.values():
            for error in field_errors:
                flash(error, 'danger')
        
    return render_template('auth/register.html', title='Kayıt Ol', form=form)
    
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Geçersiz e-posta veya şifre', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
        
    return render_template('auth/login.html', title='Giriş Yap', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))