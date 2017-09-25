from bottle import route, run, template, response, redirect, request, static_file, url, app
from beaker.middleware import SessionMiddleware

import session_util as util

#import bottle_session
import uni_common_tools.lib.Passworder as Passworder

session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.cookie_expires': 2,
    'session.auto': True
}

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
  # userid = request.forms.get('id') で取ると日本語が文字化けする
  userid = request.forms.id
  password = request.forms.password
  #pw = Passworder.Passworder()
  #encrypted_text = pw._encrypt(password)

  #role = get_role(userid, password)
  # TODO:get_roleを実装する。（DBに問い合わせと認証をするメソッド）
  role = "hoge"
  if role is not None:
    util.session_set("userid", userid)
    util.session_set("role", role)
    util.session_set('message', 'こんにちは、{} さん'.format(userid))
    return redirect('/top')
  else:
    return {'message':'ID か Password が間違っています。'}
  

@route('/top')
def top():
  '''TOP page'''
  role = util.session_get('role')
  if role is not None:
    return {'message': util.session_get('message', True),
            'role': role}
  else:
    util.session_set('message', 'ログインが必要です')
    return redirect('/login')

@route('/hoge')
def hoge():
  #s = request.environ.get('beaker.session')
  #s['test'] = s.get('test',0) + 1
  #s.save()
  test = util.session_set('test', "this is session")
  test = util.session_get('test', delete=True)
  print ("1")
  print (test)
  test = util.session_get('test', delete=True)
  print ("2")
  print (test)
  test = util.session_get('test', delete=True)
  return 'Test counter: '
  #return 'Test counter: %d' % s['test']
  #return request.environ.get('beaker.session')

app = app()
app = SessionMiddleware(app, session_opts)
run(app=app, reloader=True, port=9999)
#run(reloader=True, port=9999)
