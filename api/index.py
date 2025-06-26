import sys
import os

# 상위 디렉토리를 sys.path에 추가하여 blogpage 모듈을 import할 수 있도록 함
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blogpage import app

# Vercel serverless function handler
app = app

def handler(request):
    return app(request.environ, lambda status, headers: None) 