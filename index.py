from blogpage import app

# Vercel에서 요구하는 application 변수
application = app

if __name__ == "__main__":
    app.run(debug=False) 