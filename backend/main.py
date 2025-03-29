from web import app as web_app

app = web_app.create_app()

if __name__ == '__main__':
    app.run(debug=True)
