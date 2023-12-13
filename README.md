

  # **오늘, 내일 (Today, Tomorrow)**

  <div align="right">
  opensource programming 3분반
</div>

 

## ❓ 프로젝트 개요   
- **오늘, 내일**은  <u>**오늘 내일로 이어지는 앞으로의 일정을 관리해준다**</u>는 의미와   <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u>**"오늘 나의 일"이라는 오늘, 내 일**</u>이라는 뜻의 중의적 의미

 - **투두리스트 형식**에 **블로그 형식의 일기**를 추가한 <u>일정 관리 어플리케이션</u>
- 사용자의 일정을 관리하고, 효율적인 시간 관리를 위한 <u>투두리스트 형식</u>
- 하루에대한 성찰과 반성을 위한 <u>블로그 형식의 일기</u>
- *간단하게 일정을 추가하고 미처 완료하지 못한 일들과 완료한 일에 대한 피드백을 스스로 제공*  

<br>

## 🙋‍♀️ 설치 및 실행 방법 (원본 참고 추후 수정 예정) 
### Installation

1. 다운로드한 ZIP 파일을 압축 해제하고, 해당 디렉토리로 이동
```python
cd "해당 디렉토리"
```
2. 가상 환경을 생성  
```python
python -m venv venv

venv\Scripts\activate
```
3. 필요한 패키지 설치
```python
pip install -r requirements.txt
```
4. 애플리케이션을 실행
```python
pip install -r requirements.txt
``` 
5. 웹 브라우저에서 "http://127.0.0.1:5000"에 접속하여 Today, Tomorrow를 사용할 수 있습니다!
<br>

## 🛠 기능 설명   

### 이 어플의 핵심 기능은 5가지로 구성되어 있다
<br>

- 오늘의 할 일(체크 개수에 따라 점수 매기기)   
- 오늘을 돌아보며(블로그 형식의 일기)
- 이번 주 / 이번 달 목표
- 오늘의 명언 (처음 시작 시 랜덤으로 전시되도록)

### Flowchart

<br>

![flowchart](https://github.com/tmddbs/Today-Tomorrow/assets/75741576/1cf65aea-45a2-4a40-8f66-4ae66f3703f3)

## 프로젝트 구조


- 이 프로젝트는 'main.py', 'models.py',  'views.py', 'templates/', 'static/', 'venv/' 등의 파일들로 구성되어 있다. 

- `main.py` :  Flask 애플리케이션을 생성하고, 라우트를 등록하며, 서버를 실행
- `models.py` : 데이터베이스 모델을 정의, SQLAlchemy를 사용
- `views.py` : Flask 애플리케이션의 라우트를 정의하는 파일
- `templates/` : HTML 템플릿 파일들이 위치
- `static/` : 정적 파일들 (CSS, JavaScript, 이미지 등)이 위치하는 디렉토리
- `venv/` : 가상 환경 디렉토리

<br>

## 피드백



**버그, 질문, 의견** 등과 같은 모든 피드백은 이<u> **Repository에서 issue로 보고**</u>할 수 있다. 보고 후 조치 예정
   <br>
<br>
<br>

