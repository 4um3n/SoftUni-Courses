class Request:
    def __init__(self, path: str, method: str) -> None:
        self.path = path
        self.method = method


def get_paths():
    end_command = "END"
    paths = {}
    path_data = input()

    while path_data != end_command:
        path = path_data[:path_data.rindex("/")]
        allowed_method = path_data[path_data.rindex("/")+1:].upper()
        if path not in paths:
            paths[path] = []
        paths[path].append(allowed_method)
        path_data = input()

    return paths


def read_request():
    method, path, *_ = input().split()
    return Request(path, method)


def make_request(paths, request):
    if request.path not in paths or request.method not in paths[request.path]:
        return f"HTTP/1.1 404 Not Found\n" \
               f"Content-Length: 9\n" \
               f"Content-Type: text/plain\n\n" \
               f"Not Found"
    return f"HTTP/1.1 200 OK\n" \
           f"Content-Length: 2\n" \
           f"Content-Type: text/plain\n\n" \
           f"OK"


def get_result():
    paths = get_paths()
    request = read_request()
    result = make_request(paths, request)
    return result


print(get_result())

