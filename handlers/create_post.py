# def create_post(request):
#     body = request.split("\r\n\r\n")[-1]
#
#     return f"""HTTP/1.1 200 OK
# Content-Type: text/html
#
# <h1>Post yaratildi ✅</h1>
# <p>{body}</p>
# <a href="/">Orqaga</a>
# """
def create_post(request):
    body = request.split("\r\n\r\n")[-1]

    return f"""HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Post Created</title>

<style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #00c9a7, #92fe9d);
        text-align: center;
        color: #333;
    }}

    .container {{
        margin-top: 100px;
        background: white;
        padding: 30px;
        border-radius: 15px;
        display: inline-block;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }}

    h1 {{
        color: green;
    }}

    .post {{
        margin: 20px 0;
        padding: 15px;
        background: #f5f5f5;
        border-radius: 10px;
        font-size: 18px;
    }}

    a {{
        display: inline-block;
        margin-top: 15px;
        padding: 10px 20px;
        background: #333;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        transition: 0.3s;
    }}

    a:hover {{
        background: #000;
    }}
</style>
</head>

<body>

<div class="container">
    <h1>✅ Post yaratildi</h1>

    <div class="post">
        {body}
    </div>

    <a href="/">⬅ Orqaga</a>
</div>

</body>
</html>
"""