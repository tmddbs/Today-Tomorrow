from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import secrets
from flask_login import LoginManager

# SQLAlchemy 객체 생성
db = SQLAlchemy()
DB_NAME = "database.db"

# Flask 애플리케이션을 생성하는 함수
def create_app():
    # Flask 애플리케이션 객체 생성
    app = Flask(__name__)
    
    # 애플리케이션의 보안을 위한 임의의 비밀 키 설정
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    
    # SQLite 데이터베이스 파일 경로 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # SQLAlchemy 객체를 애플리케이션과 연결
    db.init_app(app)

    # 로그인 관리를 위한 LoginManager 객체 생성
    login_manager = LoginManager()
    
    # 로그인이 필요한 뷰를 설정
    login_manager.login_view = 'auth.login'
    
    # LoginManager 객체를 애플리케이션과 연결
    login_manager.init_app(app)

    # 사용자 로드 함수 정의
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # 라우트와 관련된 뷰 함수를 포함한 블루프린트 등록
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # 데이터베이스 모델 클래스 import
    from .models import User, Task

    # 데이터베이스 생성 함수 호출
    create_database(app)

    # 로그인 관리를 위한 LoginManager 객체 재정의
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    

    # 사용자 로드 함수 재정의
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Flask 애플리케이션 객체 반환
    return app

# 데이터베이스 생성 함수
def create_database(app):
    # 데이터베이스 파일이 존재하지 않을 경우에만 데이터베이스 생성
    if not path.exists('todolist/' + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
