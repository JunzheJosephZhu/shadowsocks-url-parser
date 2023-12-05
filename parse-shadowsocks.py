import requests
import base64
import json

def decode_shadowsocks_url(ss_url):
    # Splitting the URL to extract the encoded part
    encoded_part = ss_url.split('ss://')[1].split('@')[0]
    # Decoding the base64 part
    decoded = base64.b64decode(encoded_part).decode('utf-8')
    method, password = decoded.split(':')
    return method, password

def create_config_file(method, password, server, port, config_id):
    config = {
        "server": server,
        "server_port": int(port),
        "local_port": 1080,
        "password": password,
        "timeout": 300,
        "method": method
    }
    with open(f'ss_config_{config_id}.json', 'w') as file:
        json.dump(config, file, indent=4)

def main():
    with open('url.txt', 'r') as file:
        url = file.read()
    response = requests.get(url)
    
    if response.status_code == 200:
        ss_urls = base64.b64decode(response.text).decode("utf-8").splitlines()
        for config_id, ss_url in enumerate(ss_urls, start=1):
            method, password = decode_shadowsocks_url(ss_url)
            server_port_part = ss_url.split('@')[1].split('#')[0]
            server, port = server_port_part.split(':')
            create_config_file(method, password, server, port, config_id)
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")

if __name__ == "__main__":
    main()

