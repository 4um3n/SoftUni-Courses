from urllib import parse


valid_ports = {
    "http": ["80"],
    "https": ["443", "447"],
}
parsed_uri = parse.urlparse(input())
protocol = parsed_uri.scheme
host_port = parsed_uri.netloc
host, port = None, None
path = parsed_uri.path
path = "/" if not path else path
query = parsed_uri.query
fragment = parsed_uri.fragment

if ":" in host_port:
    host, port = host_port.split(":")
elif protocol in valid_ports:
    host, port = host_port, valid_ports[protocol][0]

if not protocol or not host or not port or not path or port not in valid_ports[protocol]:
    print(f"Invalid URL")
    exit()

info = [
    f"Protocol: {protocol}",
    f"Host: {host}",
    f"Port: {port}",
    f"Path: {path}",
]

if query:
    info.append(f"Query: {query}")
if fragment:
    info.append(f"Fragment: {fragment}")

print('\n'.join(info))
