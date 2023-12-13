from . import db  # db 모듈 import
from flask_login import UserMixin  # Flask-Login의 UserMixin 상속
from sqlalchemy.sql import func  # SQLAlchemy의 func 모듈 import


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 작업 ID (기본 키)
    title = db.Column(db.String(30))  # 작업 제목 (문자열, 최대 길이 30)
    description = db.Column(db.String(1000))  # 작업 설명 (문자열, 최대 길이 1000)
    complete = db.Column(db.Boolean, default=False)  # 작업 완료 여부 (부울 값, 기본값 False)
    created = db.Column(db.DateTime(timezone=True), default=func.now())  # 작업 생성 일시 (날짜와 시간, 기본값 현재 시간)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 작업을 소유하는 사용자의 ID (외래 키)
    

    def __repr__(self):
        return self.title  # 작업 객체를 문자열로 표현할 때 제목을 반환
    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # 사용자 ID (기본 키)
    email = db.Column(db.String(100), unique=True)  # 사용자 이메일 (문자열, 최대 길이 100, 고유한 값)
    password = db.Column(db.String(150))  # 사용자 비밀번호 (문자열, 최대 길이 150)
    first_name = db.Column(db.String(150))  # 사용자 이름 (문자열, 최대 길이 150)
    tasks = db.relationship('Task', lazy=True, backref='tasks')  # 사용자와 작업 간의 관계 설정







