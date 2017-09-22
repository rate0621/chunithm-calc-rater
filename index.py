from bottle import route, run, template, response, redirect, request, static_file, url
import src.lib.Passworder as Passworder

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def index():
  redirect ("/login", 301)

@route('/login')
def login():
  return template("login")

@route('/login', method="POST")
def login():
  # username = request.forms.get('id') で取ると日本語が文字化けする
  username = request.forms.id
  password = request.forms.password

  pw = Passworder.Passworder()
  encrypted_text = pw._encrypt(password)

  return ("id is " +  username + ", password is " + encrypted_text)

run(reloader=True, port=9999)
