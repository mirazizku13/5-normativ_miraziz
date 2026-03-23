# def home():
#     return """HTTP/1.1 200 OK
# Content-Type: text/html
#
# <h1>Bosh sahifa 🏠</h1>
# <form method="POST" action="/create">
#     <input type="text" name="title" placeholder="Title">
#     <button type="submit">Yuborish</button>
# </form>
# """
def home():
    return """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My Website</title>

<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        text-align: center;
    }

    .container {
        margin-top: 100px;
        background: rgba(0,0,0,0.3);
        padding: 30px;
        border-radius: 15px;
        display: inline-block;
    }

    h1 {
        margin-bottom: 10px;
    }

    input {
        padding: 10px;
        width: 200px;
        border-radius: 5px;
        border: none;
        margin: 10px;
    }

    button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        background: #00c9a7;
        color: white;
        cursor: pointer;
        transition: 0.3s;
    }

    button:hover {
        background: #00a78e;
    }

    .footer {
        margin-top: 30px;
        font-size: 14px;
        opacity: 0.7;
    }
</style>
</head>

<body>

<div class="container">
    <h1>🏠 Bosh sahifa</h1>
    <p>Post qo‘shish</p>

    <form method="POST" action="/create">
        <input type="text" name="title" placeholder="Title yozing..." required>
        <br>
        <button type="submit">🚀 Yuborish</button>
    </form>

    <div class="footer">
        © 2026 Miraziz
    </div>
</div>

</body>
</html>
"""