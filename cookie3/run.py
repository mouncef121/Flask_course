from flask import Flask, redirect, render_template, request, url_for, make_response

app  = Flask(__name__)

@app.route('/')
def home():
    theme = request.cookies.get('theme','clair')
    return render_template('home.html', theme = theme)

@app.route('/set_theme/<theme>')
def set_theme(theme):
    resp = make_response(redirect('/'))
    resp.set_cookie('theme', theme)
    return resp

@app.route('/reset_theme')
def reset_theme():
    resp = make_response(redirect('/'))
    resp.delete_cookie('theme')
    return resp

if __name__ == '__main__':
    app.run(debug=True)