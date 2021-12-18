from urllib import parse


url_data = input()
print(parse.unquote(url_data))
