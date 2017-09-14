from bottle import route, run, template, response, redirect, request
import test

@route('/')
def index():
  redirect ("http://localhost:9999/login", 301)
  #return "<h1>WELCOME </h1>"
  #return template('<b>Hello {{name}}</b>!', name=name)

@route('/login')
def login():
  username = request.query.get('user')
  password = request.query.get('pass')

  #GETで何も渡されていない時はusername,passwordに何も入れない
  username = "" if username is None else username
  password = "" if password is None else password

  tc = Test.TestClass(username, password)
  hoge, huga = tc.hoge()

  return '''
    <form action="/login" method="post">
            Username: <input name="username" type="text" value="{username}"/>
            Password: <input name="password" type="password" value="{password}"/>
            <input value="Login" type="submit" />
        </form>
  '''.format(username=hoge, password=huga)

@route('/top')
def top():
  item_list = [
    {"id": 1, "name": "ringo",  "color": "red"},
    {"id": 2, "name": "banana", "color": "yellow"},
    {"id": 3, "name": "orange", "color": "orange"}
  ]

  return template("tpl/list_tmpl", item_list=item_list)


#@route('/r2')
#def r2_test():
#
#  response.status = 302
#  redirect_url = '{0}://login'.format(
#                  request.urlparts.scheme, request.urlparts.netloc)
#  response.set_header('Location', redirect_url)
#  return response

#run(host='localhost', port=8080)
run(reloader=True, port=9999)
