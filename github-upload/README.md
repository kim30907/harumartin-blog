# 하루마틴 블로그 시스템

딸아이와 함께하는 소중한 순간들을 기록하는 개인 블로그 시스템입니다.

## 🌟 주요 기능

### 📝 고급 글 작성 시스템
- **HTML 에디터**: 코드로 직접 글 작성 가능
- **실시간 미리보기**: 작성 중인 글을 즉시 확인
- **이미지 업로드**: 다중 파일 업로드 및 관리
- **썸네일 설정**: 업로드된 이미지 중 썸네일 선택
- **이미지 삽입**: 에디터 내 원하는 위치에 이미지 삽입

### ⏰ 예약 발행
- 날짜와 시간을 설정하여 예약 발행 가능
- 즉시 발행, 임시 저장, 예약 발행 옵션

### 🎨 티스토리 스타일 디자인
- 전문적인 블로그 스타일 적용
- Gowun Dodum 폰트 사용
- 다양한 HTML 요소 스타일링 (제목, 인용문, 표, 글상자 등)

### 📱 반응형 디자인
- 모바일, 태블릿, 데스크톱 모든 기기 지원
- 직관적인 사용자 인터페이스

## 🚀 기술 스택

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Font**: Gowun Dodum (Google Fonts)
- **Icons**: Font Awesome

## 📦 설치 및 실행

### 1. 필요 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 서버 실행
```bash
python blogpage.py
```

### 3. 브라우저에서 접속
- **메인 사이트**: `http://127.0.0.1:8080`
- **관리자 페이지**: `http://127.0.0.1:8080/admin`

## 🔑 관리자 로그인

- **아이디**: `kim30907`
- **비밀번호**: `rlatmdwls88!`

## 📁 프로젝트 구조

```
github-upload/
├── blogpage.py              # 메인 Flask 애플리케이션
├── requirements.txt         # 패키지 의존성
├── static/
│   └── images/
│       ├── uploads/         # 업로드된 이미지
│       ├── 12.png          # 히어로 섹션 배경
│       └── logo.png        # 로고
├── templates/
│   ├── index.html          # 메인 페이지
│   ├── admin_simple.html   # 관리자 대시보드
│   ├── post_detail.html    # 포스트 상세 페이지
│   ├── admin_login.html    # 관리자 로그인
│   ├── 404.html           # 404 에러 페이지
│   └── 500.html           # 500 에러 페이지
└── data/                   # 데이터 파일들
```

## ✨ 사용 가능한 HTML 스타일

### 제목
```html
<h1>페이지 메인 제목</h1>
<h2>주요 섹션 제목</h2>
<h3>하위 제목</h3>
<h4>소제목</h4>
```

### 특수 박스
```html
<!-- 글상자 -->
<div class="text-box"><p>강조 내용</p></div>

<!-- 경고상자 -->
<div class="alert-box"><strong>주의:</strong> 경고 내용</div>

<!-- Q&A -->
<div class="qa-box">
  <p class="question">Q: 질문</p>
  <p class="answer">A: 답변</p>
</div>
```

### 인용문
```html
<blockquote>인용 내용</blockquote>
```

## 🔗 소셜 미디어 연결

- **인스타그램**: [@harumartin88](https://www.instagram.com/harumartin88/)
- **유튜브**: [하루마틴 채널](https://www.youtube.com/channel/UC3xaz_6w0aI0pVKuJ2gAXnA)

## 📝 라이선스

이 프로젝트는 개인 블로그 목적으로 제작되었습니다.

---

*딸아이와 함께하는 소중한 순간들을 기록하는 하루마틴 블로그* ❤️ 