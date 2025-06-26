# 하루마틴 블로그 🌸

> 딸아이와의 하루를 기록하는 따뜻한 블로그

## 프로젝트 소개

하루마틴은 아빠 마틴이 5살 딸아이와 함께하는 일상을 기록하고 공유하는 감성적인 블로그입니다. 
따뜻한 파스텔 톤의 디자인과 부드러운 사용자 경험을 통해 육아의 소중한 순간들을 아름답게 담아냅니다.

## 주요 기능

### ✨ 디자인 특징
- 따뜻한 파스텔 톤 (연핑크, 베이지 계열) 색상 팔레트
- 둥글고 부드러운 모던 디자인
- 반응형 웹 디자인 (모바일, 태블릿, 데스크톱 지원)
- 부드러운 애니메이션과 호버 효과

### 📱 주요 섹션
1. **헤더**: 고정된 네비게이션 바 with 스크롤 효과
2. **히어로 섹션**: 메인 배너와 CTA 버튼
3. **Martin's Log**: 최근 일상 포스팅 카드
4. **Martin's Tip**: 육아 꿀팁 섹션
5. **추천 영상**: 유튜브 영상 썸네일
6. **About**: 마틴 소개
7. **푸터**: 연락처 및 소셜 링크

### 🎯 인터랙티브 기능
- 부드러운 스크롤 네비게이션
- 모바일 햄버거 메뉴
- 스크롤 진행률 표시
- 카드 호버 애니메이션
- 버튼 리플 효과
- 스크롤 기반 요소 애니메이션

## 기술 스택

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Noto Sans KR (Google Fonts)
- **Icons**: Font Awesome 6
- **Images**: Unsplash API

## 설치 및 실행

### 1. 저장소 클론
```bash
git clone <repository-url>
cd harumartin88-blog
```

### 2. 가상환경 생성 및 활성화
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python blogpage.py
```

### 5. 브라우저에서 확인
```
http://localhost:5000
```

## 프로젝트 구조

```
harumartin88-blog/
├── blogpage.py              # Flask 메인 애플리케이션
├── requirements.txt         # Python 패키지 의존성
├── README.md               # 프로젝트 문서
├── templates/
│   └── index.html          # 메인 HTML 템플릿
└── static/
    ├── css/
    │   └── style.css       # 메인 스타일시트
    ├── js/
    │   └── script.js       # JavaScript 기능
    └── images/             # 이미지 파일들
```

## 커스터마이징

### 색상 변경
`static/css/style.css` 파일의 `:root` 섹션에서 CSS 변수를 수정하세요:

```css
:root {
    --primary-color: #ff9a9e;      /* 메인 색상 */
    --secondary-color: #fecfef;    /* 보조 색상 */
    --accent-color: #ffecd2;       /* 강조 색상 */
    /* ... */
}
```

### 콘텐츠 수정
`blogpage.py` 파일의 샘플 데이터를 수정하여 실제 콘텐츠로 교체하세요:

```python
recent_posts = [
    {
        'title': '새로운 포스트 제목',
        'date': '2025-01-15',
        'thumbnail': '이미지 URL',
        'summary': '포스트 요약'
    },
    # ...
]
```

## 배포

### Heroku 배포
1. Heroku CLI 설치
2. `Procfile` 생성:
   ```
   web: python blogpage.py
   ```
3. Git 저장소 초기화 및 Heroku 앱 생성
4. 배포 실행

### Vercel 배포
1. `vercel.json` 설정 파일 생성
2. Vercel CLI로 배포

## 향후 개발 계획

- [ ] 관리자 패널 구현
- [ ] 데이터베이스 연동 (SQLite/PostgreSQL)
- [ ] 댓글 시스템
- [ ] 검색 기능
- [ ] 다크 모드
- [ ] PWA 지원
- [ ] SEO 최적화

## 라이선스

이 프로젝트는 개인 사용을 위한 것입니다.

## 연락처

- **블로그**: 하루마틴
- **운영자**: 아빠 마틴
- **이메일**: martin@harumartin88.blog
- **인스타그램**: [@harumartin88](https://instagram.com/harumartin88)
- **유튜브**: [@harumartin88](https://youtube.com/@harumartin88)

---

💝 **딸아이와의 소중한 하루하루를 기록하며, 따뜻한 추억을 만들어갑니다.** 