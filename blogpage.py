from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid
from functools import wraps

app = Flask(__name__)
app.secret_key = 'harumatin-secret-key-2025'  # 실제 운영시에는 환경변수로 설정하세요

# 관리자 계정 정보
ADMIN_ID = 'kim30907'
ADMIN_PW = 'rlatmdwls88!'

# 로그인 확인 데코레이터
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# 설정
UPLOAD_FOLDER = 'static/images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
DATA_FOLDER = 'data'

# 디렉토리 생성
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)

# 파일 확장자 확인
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 데이터 파일 경로
POSTS_FILE = os.path.join(DATA_FOLDER, 'posts.json')
CATEGORIES_FILE = os.path.join(DATA_FOLDER, 'categories.json')

# 기본 카테고리 설정
DEFAULT_CATEGORIES = {
    'daily-life': {
        'name': '일상 기록',
        'description': '딸아이와의 소중한 일상을 기록합니다',
        'type': 'log'
    },
    'growth': {
        'name': '성장 기록',
        'description': '딸아이의 성장 과정을 기록합니다',
        'type': 'log'
    },
    'parenting-tips': {
        'name': '육아 꿀팁',
        'description': '실용적인 육아 노하우를 공유합니다',
        'type': 'tip'
    },
    'baby-care': {
        'name': '아기 돌보기',
        'description': '아기 돌봄에 관한 팁을 공유합니다',
        'type': 'tip'
    }
}

# 데이터 로드/저장 함수들
def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_posts(posts):
    with open(POSTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

def load_categories():
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        save_categories(DEFAULT_CATEGORIES)
        return DEFAULT_CATEGORIES

def save_categories(categories):
    with open(CATEGORIES_FILE, 'w', encoding='utf-8') as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)

@app.route('/')
def home():
    posts = load_posts()
    
    # 최근 포스트 (Martin's Log - log 타입)
    recent_posts = [post for post in posts if post.get('post_type') == 'log' and post.get('status') == '발행됨'][:3]
    
    # 육아 팁 (Martin's Tip - tip 타입)
    parenting_tips = [post for post in posts if post.get('post_type') == 'tip' and post.get('status') == '발행됨'][:3]
    
    # 실제 유튜브 채널 비디오
    youtube_videos = [
        {
            'title': '하루마틴 - 딸과 함께하는 일상 브이로그',
            'thumbnail': 'https://images.unsplash.com/photo-1511988617509-a57c8a288659?w=400&h=250&fit=crop',
            'url': 'https://www.youtube.com/channel/UC3xaz_6w0aI0pVKuJ2gAXnA',
            'channel_url': 'https://www.youtube.com/channel/UC3xaz_6w0aI0pVKuJ2gAXnA'
        },
        {
            'title': '아빠표 육아 노하우',
            'thumbnail': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400&h=250&fit=crop',
            'url': 'https://www.youtube.com/channel/UC3xaz_6w0aI0pVKuJ2gAXnA',
            'channel_url': 'https://www.youtube.com/channel/UC3xaz_6w0aI0pVKuJ2gAXnA'
        }
    ]
    
    return render_template('index.html', 
                         recent_posts=recent_posts,
                         parenting_tips=parenting_tips,
                         youtube_videos=youtube_videos)

@app.route('/martins-log')
def martins_log():
    posts = load_posts()
    log_posts = [post for post in posts if post.get('post_type') == 'log' and post.get('status') == '발행됨']
    log_posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    return render_template('martins_log.html', posts=log_posts)

@app.route('/martins-tip')
def martins_tip():
    posts = load_posts()
    tip_posts = [post for post in posts if post.get('post_type') == 'tip' and post.get('status') == '발행됨']
    tip_posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    return render_template('martins_tip.html', tips=tip_posts)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_ID and password == ADMIN_PW:
            session['logged_in'] = True
            session['username'] = username
            flash('로그인 성공!')
            return redirect(url_for('admin'))
        else:
            flash('아이디 또는 비밀번호가 잘못되었습니다.')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('로그아웃되었습니다.')
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    posts = load_posts()
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    return render_template('admin.html', posts_list=posts)

@app.route('/admin/write')
@login_required
def admin_write():
    categories = load_categories()
    return render_template('admin.html', active_tab='write', categories=categories)

@app.route('/admin/posts')
@login_required
def admin_posts():
    posts = load_posts()
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    return render_template('admin.html', active_tab='posts', posts_list=posts)

@app.route('/admin/settings')
@login_required
def admin_settings():
    categories = load_categories()
    return render_template('admin.html', active_tab='settings', categories=categories)

# 개별 포스트 페이지
@app.route('/post/<post_id>')
def view_post(post_id):
    posts = load_posts()
    post = next((post for post in posts if post.get('id') == post_id), None)
    
    if not post:
        flash('존재하지 않는 글입니다.')
        return redirect(url_for('home'))
    
    # 관련 포스트 (같은 타입의 다른 글들)
    related_posts = [p for p in posts if p.get('post_type') == post.get('post_type') and p.get('id') != post_id][:3]
    
    return render_template('post_detail.html', post=post, related_posts=related_posts)

# 글 저장 API
@app.route('/api/save-post', methods=['POST'])
@login_required
def save_post():
    try:
        data = request.get_json()
        
        # 필수 필드 검증
        if not data.get('title') or not data.get('category') or not data.get('content'):
            return jsonify({'success': False, 'message': '제목, 카테고리, 내용은 필수입니다.'})
        
        posts = load_posts()
        
        # 새 포스트 생성
        post = {
            'id': str(uuid.uuid4()),
            'title': data['title'],
            'category': data['category'],
            'subcategory': data.get('subcategory', ''),
            'content': data['content'],
            'summary': data.get('summary', ''),
            'thumbnail': data.get('thumbnail', ''),
            'tags': data.get('tags', []),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'created_at': datetime.now().isoformat(),
            'status': data.get('status', '발행됨'),
            'editor_type': data.get('editor_type', 'wysiwyg')
        }
        
        # 카테고리 타입 확인하여 추가 필드 설정
        categories = load_categories()
        category_info = categories.get(data['category'], {})
        
        # Tip 타입 카테고리인 경우 추가 필드
        if category_info.get('type') == 'tip':
            post['difficulty'] = data.get('difficulty', '보통')
            post['time'] = data.get('time', '')
            post['post_type'] = 'tip'
        else:
            post['post_type'] = 'log'
        
        posts.append(post)
        save_posts(posts)
        
        return jsonify({'success': True, 'message': '글이 성공적으로 저장되었습니다.', 'post_id': post['id']})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'저장 중 오류가 발생했습니다: {str(e)}'})

# 이미지 업로드 API
@app.route('/api/upload-image', methods=['POST'])
@login_required
def upload_image():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': '파일이 선택되지 않았습니다.'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'message': '파일이 선택되지 않았습니다.'})
        
        if file and allowed_file(file.filename):
            # 안전한 파일명 생성
            filename = secure_filename(file.filename)
            # 고유한 파일명 생성 (중복 방지)
            name, ext = os.path.splitext(filename)
            unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
            
            file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            file.save(file_path)
            
            # 웹에서 접근 가능한 URL 생성
            file_url = f"/static/images/uploads/{unique_filename}"
            
            return jsonify({
                'success': True, 
                'message': '이미지가 성공적으로 업로드되었습니다.',
                'file_url': file_url,
                'filename': unique_filename
            })
        else:
            return jsonify({'success': False, 'message': '지원하지 않는 파일 형식입니다. (PNG, JPG, JPEG, GIF, WEBP만 가능)'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'업로드 중 오류가 발생했습니다: {str(e)}'})

# 카테고리 관리 API
@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = load_categories()
    return jsonify({'success': True, 'categories': categories})

@app.route('/api/categories', methods=['POST'])
@login_required
def add_category():
    try:
        data = request.get_json()
        categories = load_categories()
        
        category_id = data.get('id')
        category_name = data.get('name')
        category_desc = data.get('description', '')
        category_type = data.get('type', 'log')  # 기본값은 'log'
        
        if not category_id or not category_name:
            return jsonify({'success': False, 'message': '카테고리 ID와 이름은 필수입니다.'})
        
        if category_id in categories:
            return jsonify({'success': False, 'message': '이미 존재하는 카테고리 ID입니다.'})
        
        # 타입 검증
        if category_type not in ['log', 'tip']:
            return jsonify({'success': False, 'message': '카테고리 타입은 log 또는 tip이어야 합니다.'})
        
        categories[category_id] = {
            'name': category_name,
            'description': category_desc,
            'type': category_type
        }
        
        save_categories(categories)
        return jsonify({'success': True, 'message': '카테고리가 추가되었습니다.'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'카테고리 추가 중 오류가 발생했습니다: {str(e)}'})

@app.route('/api/categories/<category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    try:
        categories = load_categories()
        
        if category_id not in categories:
            return jsonify({'success': False, 'message': '존재하지 않는 카테고리입니다.'})
        
        # 해당 카테고리의 글이 있는지 확인
        posts = load_posts()
        category_posts = [post for post in posts if post.get('category') == category_id]
        
        if category_posts:
            return jsonify({'success': False, 'message': f'해당 카테고리에 {len(category_posts)}개의 글이 있어 삭제할 수 없습니다.'})
        
        del categories[category_id]
        save_categories(categories)
        
        return jsonify({'success': True, 'message': '카테고리가 삭제되었습니다.'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'카테고리 삭제 중 오류가 발생했습니다: {str(e)}'})

@app.route('/api/categories/<category_id>/subcategories', methods=['POST'])
@login_required
def add_subcategory(category_id):
    try:
        data = request.get_json()
        categories = load_categories()
        
        if category_id not in categories:
            return jsonify({'success': False, 'message': '존재하지 않는 카테고리입니다.'})
        
        subcategory = data.get('subcategory')
        if not subcategory:
            return jsonify({'success': False, 'message': '서브카테고리 이름은 필수입니다.'})
        
        if subcategory in categories[category_id]['subcategories']:
            return jsonify({'success': False, 'message': '이미 존재하는 서브카테고리입니다.'})
        
        categories[category_id]['subcategories'].append(subcategory)
        save_categories(categories)
        
        return jsonify({'success': True, 'message': '서브카테고리가 추가되었습니다.'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'서브카테고리 추가 중 오류가 발생했습니다: {str(e)}'})

# 글 삭제 API
@app.route('/api/posts/<post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    try:
        posts = load_posts()
        posts = [post for post in posts if post.get('id') != post_id]
        save_posts(posts)
        
        return jsonify({'success': True, 'message': '글이 삭제되었습니다.'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'글 삭제 중 오류가 발생했습니다: {str(e)}'})

# 글 편집을 위한 데이터 로드 API
@app.route('/api/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    try:
        posts = load_posts()
        post = next((post for post in posts if post.get('id') == post_id), None)
        
        if not post:
            return jsonify({'success': False, 'message': '글을 찾을 수 없습니다.'})
        
        return jsonify({'success': True, 'post': post})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'글 로드 중 오류가 발생했습니다: {str(e)}'})

# 404 에러 핸들러 추가
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# 500 에러 핸들러 추가
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# 정적 파일 라우트 추가 (배포 환경에서 필요할 수 있음)
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

# 루트 경로에서 favicon 처리
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# Vercel 배포를 위한 app 인스턴스 노출
app = app

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
