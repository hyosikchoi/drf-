from django.apps import AppConfig


# Django에서 apps.py의 역할:
#
# AppConfig의 핵심 기능:
# 1. 앱 식별: Django가 해당 디렉토리를 앱으로 인식하게 함
# 2. 앱 설정: 앱의 메타데이터와 동작 방식을 정의
# 3. 초기화: 앱이 로드될 때 실행할 코드 정의

# 없으면 생기는 문제:
# - Django가 앱을 인식하지 못함
# - 마이그레이션이 생성되지 않음
# - 모델이 DB에 반영되지 않음
# - INSTALLED_APPS에 등록해도 무시됨

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # 기본 PK 필드 타입
    name = 'domains.accounts'   # 앱의 풀 Python 경로
