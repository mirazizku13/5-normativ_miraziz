def not_found():
    return """HTTP/1.1 404 Not Found
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404 Not Found</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #e5e5e5;
            text-align: center;
        }

        .container {
            margin-top: 100px;
        }

        h1 {
            font-size: 100px;
            color: #333;
            margin: 0;
        }

        h2 {
            color: #555;
        }

        p {
            color: #777;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #333;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }

        a:hover {
            background-color: #000;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>404</h1>
        <h2>Page Not Found</h2>
        <p>Kechirasiz, bu sahifa mavjud emas.</p>

        <a href="http://127.0.0.1:8080">Go Home</a>
    </div>

</body>
</html>
"""