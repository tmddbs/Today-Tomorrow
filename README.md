

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

The repository can be included as a [Poetry](https://python-poetry.org/) dependency in `pyproject.toml`.
It is best to integrate to a release tag to ensure a stable dependency:

```toml
[tool.poetry.dependencies]
todoist-api-python = "^v2.0.0"
```

### Supported Python Versions

Python 3.9 is fully supported and tested, and while it may work with other Python 3 versions, we do not test for them.

### Usage

An example of initializing the API client and fetching a user's tasks:

```python
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI

# Fetch tasks asynchronously
async def get_tasks_async():
    api = TodoistAPIAsync("YOURTOKEN")
    try:
        tasks = await api.get_tasks()
        print(tasks)
    except Exception as error:
        print(error)

# Fetch tasks synchronously
def get_tasks_sync():
    api = TodoistAPI("my token")
    try:
        tasks = api.get_tasks()
        print(tasks)
    except Exception as error:
        print(error)
```
<br>

## 🛠 기능 설명   

### 이 어플의 핵심 기능은 5가지로 구성되어 있다
<br>

- 오늘의 할 일(체크 개수에 따라 점수 매기기)   

- 오늘을 돌아보며(블로그 형식의 일기) – 오늘의 표정
- 이번 주 / 이번 달 목표 (마감 기한 설정)
- 오늘의 명언 (처음 시작 시 전시되도록)
- 하지 못한 오늘의 할 일 미루기 or 삭제

### Flowchart

<br>

![flowchart](https://github.com/tmddbs/Today-Tomorrow/assets/75741576/1cf65aea-45a2-4a40-8f66-4ae66f3703f3)

## 프로젝트 구조


- 이 프로젝트는 `.github`, `Today,Tomorrow`, `tests`, `todoist_api_python` 등의 파일들로 구성되어 있다. 

- `.github` : workflow 설정 파일들이 저장되는 폴더
- `Today,Tomorrow` : 추가적으로 제작할 파일이 들어갈 폴더
- `tests` :프로젝트의 단위 테스트 코드가 들어 있는 폴더
-  `todoist_api_python` : main 프로젝트 코드가 들어있는 폴더
-  
<br>

## 피드백



**버그, 질문, 의견** 등과 같은 모든 피드백은 이<u> **Repository에서 issue로 보고**</u>할 수 있다. 보고 후 조치 예정
   
