<link rel="stylesheet" type="text/css" href="/static/css/login.css">
<script type="text/javascript" src="static/js/login.js"></script>

<table class="list">
  <tr>
    <th>曲名</th>
    <th>難易度</th>
    <th>スコア</th>
  </tr>
  {% for key in record_list %}
  <tr>
    <td>{{ record_list[key]["music_name"] }}</td>
    <td>{{ record_list[key]["difficulty_id"] }}</td>
    <td>{{ record_list[key]["score"] }}</td>
  </tr>
  {% endfor %}
</table>
