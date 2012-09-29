<!DOCTYPE html>
<html language="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<link rel="stylesheet" type="text/css" href="/media/css/category.css"/>
</head>
    
<body>
<div id="main">

    <div id="head">
        <a href="/mobosite/retrieve/0/rencet/20/1/"><img class="home" src="/media/image/ic_home.png"/></a>
        <img class="spliter" src="/media/image/line_tab.png"/>
        <span class="title">Projects</span>
    </div>
    
    {% for project in projects %}
    <a class="item" href="/project/{{ project.id}}/">
        <img src="/media/image/ic_ringtone.png"/>
        <div class="content">
            <div class="ringtone-title">{{ project.name }}</div>
            <div class="ringtone-description">{{ project.description }}</div>
        </div>
        <div class="ringtone-size">{{ project.last_modify|date:"Y-m-d"}}</div>
    </a>
    {% endfor %}
    
    <div id="foot">
        <span>
            <a href="/media/static/about.html">about us</a> | <a href="mailto:mobodev@gmail.com">contact us</a> | <a href="/media/static/app.html">our Website</a>
        </span>
    </div>
</div>
</body>
</html>