<link rel="stylesheet" type="text/css" href="/static/css/login.css">
<script type="text/javascript" src="static/js/login.js"></script>

<div class="login">
  <div class="login-triangle"></div>
  
  <h2 class="login-header">Log in</h2>

  <form id="loginForm" class="login-container" method="post" onsubmit="return Login.doLogin(this)">
    <p>{{ test }}</p>
    <p><input type="text" name="id" placeholder="id"></p>
    <p><input type="password" name="password" placeholder="Password"></p>
    <p><input type="submit" value="Log in"></p>
  </form>
</div>
