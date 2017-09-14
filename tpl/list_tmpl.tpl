<h1>一覧</h1>
<table border="1">
%for item in item_list:
  <tr>
    <td>{{item["id"]}}</td>
    <td>{{item["name"]}}</td>
    <td>{{item["color"]}}</td>
  </tr>
%end
</table>
