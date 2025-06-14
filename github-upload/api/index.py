import sys
import os

# 상위 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blogpage import app

# Vercel serverless function handler
def handler(event, context):
    return app

# Flask 앱을 직접 노출 (Vercel이 자동으로 감지)
app = app 