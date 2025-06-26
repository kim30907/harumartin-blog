import sys
import os
import json

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from blogpage import app

def handler(event, context):
    try:
        # Netlify Functions의 이벤트를 Flask WSGI 환경으로 변환
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET')
        headers = event.get('headers', {})
        query_string = event.get('queryStringParameters') or {}
        body = event.get('body', '')
        
        # 간단한 WSGI 환경 구성
        environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'QUERY_STRING': '&'.join([f"{k}={v}" for k, v in query_string.items()]),
            'CONTENT_TYPE': headers.get('content-type', ''),
            'CONTENT_LENGTH': str(len(body)) if body else '0',
            'HTTP_HOST': headers.get('host', 'localhost'),
            'wsgi.input': None,
            'wsgi.errors': sys.stderr,
        }
        
        # Flask 앱 실행
        with app.test_client() as client:
            if method == 'GET':
                response = client.get(path, query_string=query_string, headers=headers)
            elif method == 'POST':
                response = client.post(path, data=body, headers=headers)
            else:
                response = client.open(method=method, path=path, data=body, headers=headers)
        
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        } 