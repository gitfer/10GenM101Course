<!DOCTYPE html>
<html>
<head>
<title>Hello world!</title>
</head>
<body>
<p> Welcome {{username}}
</p>
<ul>
%for thing in stuff:
<li>{{thing}}</li>
%end
</ul>
</body>
</html>
