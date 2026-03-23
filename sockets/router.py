def parse_request(request):
    lines = request.split("\n")
    first_line = lines[0]
    method, path, _ = first_line.split()
    return method, path


def route(request):
    method, path = parse_request(request)

    if path == "/" and method == "GET":
        from handlers.home import home
        return home()

    elif path == "/create" and method == "POST":
        from handlers.create_post import create_post
        return create_post(request)

    else:
        from handlers.not_found import not_found
        return not_found()