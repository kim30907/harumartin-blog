import sys
import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, send_from_directory
from functools import wraps
import json
from datetime import datetime

# Flask 앱 생성
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')
app.secret_key = 'your-secret-key-here-change-in-production'

# 메모리 기반 데이터 저장
posts_data = []
categories_data = {
    "log": [
        {"id": "daily-life", "name": "일상 기록"},
        {"id": "growth", "name": "성장 기록"}
    ],
    "tip": [
        {"id": "parenting-tips", "name": "육아 꿀팁"},
        {"id": "baby-care", "name": "아기 돌보기"}
    ]
}

# 관리자 계정 정보
ADMIN_USERNAME = 'kim30907'
ADMIN_PASSWORD = 'rlatmdwls88!'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# 정적 파일 서빙 라우트
@app.route('/static/<path:filename>')
def static_files(filename):
    try:
        # 현재 파일의 디렉토리를 기준으로 static 폴더 경로 설정
        current_dir = os.path.dirname(os.path.abspath(__file__))
        static_dir = os.path.join(current_dir, '..', 'static')
        return send_from_directory(static_dir, filename)
    except Exception as e:
        print(f"Static file error: {e}")
        return f"File not found: {filename}", 404

@app.route('/')
def home():
    # 샘플 데이터
    recent_posts = [
        {
            'title': '딸과 함께한 첫 번째 놀이공원',
            'summary': '5살 딸아이와 함께 놀이공원에 다녀온 특별한 하루',
            'date': '2025-01-15',
            'thumbnail': 'https://images.unsplash.com/photo-1551963831-b3b1ca40c98e?w=400&h=250&fit=crop'
        },
        {
            'title': '아이와 함께하는 요리 시간',
            'summary': '간단한 쿠키 만들기로 시작한 즐거운 요리 체험',
            'date': '2025-01-10',
            'thumbnail': 'https://images.unsplash.com/photo-1551963831-b3b1ca40c98e?w=400&h=250&fit=crop'
        }
    ]
    
    parenting_tips = [
        {
            'title': '아이 편식 해결하는 5가지 방법',
            'summary': '실전에서 터득한 편식 아이 식사 지도법',
            'date': '2025-01-12',
            'thumbnail': 'https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=400&h=250&fit=crop'
        }
    ]
    
    return render_template('index.html', 
                         recent_posts=recent_posts, 
                         parenting_tips=parenting_tips)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('아이디 또는 비밀번호가 올바르지 않습니다.')
    
    return render_template('admin_login.html')

@app.route('/admin')
@login_required
def admin():
    return render_template('admin_simple.html', posts_list=posts_data)

@app.route('/admin/logout')
@login_required
def admin_logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/api/save-post', methods=['POST'])
@login_required
def save_post():
    try:
        data = request.get_json()
        
        # 새 포스트 생성
        new_post = {
            'id': str(len(posts_data) + 1),
            'title': data.get('title', ''),
            'content': data.get('content', ''),
            'summary': data.get('summary', ''),
            'category': data.get('category', ''),
            'post_type': data.get('post_type', 'log'),
            'status': data.get('status', '발행됨'),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'thumbnail': 'https://images.unsplash.com/photo-1551963831-b3b1ca40c98e?w=400&h=250&fit=crop'
        }
        
        posts_data.append(new_post)
        
        return jsonify({'success': True, 'message': '글이 저장되었습니다.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/martins-log')
def martins_log():
    log_posts = [post for post in posts_data if post.get('post_type') == 'log']
    return render_template('index.html', recent_posts=log_posts[:6], parenting_tips=[])

@app.route('/martins-tip')
def martins_tip():
    tip_posts = [post for post in posts_data if post.get('post_type') == 'tip']
    return render_template('index.html', recent_posts=[], parenting_tips=tip_posts[:6])

@app.route('/post/<post_id>')
def post_detail(post_id):
    post = next((p for p in posts_data if p.get('id') == post_id), None)
    if not post:
        return render_template('404.html'), 404
    
    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>{post.get('title', '제목 없음')} - 하루마틴</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50">
        <div class="max-w-4xl mx-auto p-6">
            <div class="bg-white rounded-lg shadow-sm p-8">
                <h1 class="text-3xl font-bold mb-4">{post.get('title', '제목 없음')}</h1>
                <div class="text-gray-500 mb-6">{post.get('date', '')}</div>
                <div class="prose max-w-none">
                    {post.get('content', '내용이 없습니다.')}
                </div>
                <div class="mt-8">
                    <a href="/" class="text-blue-600 hover:text-blue-800">← 홈으로 돌아가기</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Vercel에서 사용할 핸들러
def handler(event, context):
    return app

if __name__ == '__main__':
    app.run(debug=True) 