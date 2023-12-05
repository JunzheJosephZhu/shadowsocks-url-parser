This is a library that takes a url from websites such as 白月光，and parses into configs that can be read by linux shadowsocks client.
Usage:
1. Create a file called url.txt
2. python parse-shadowsocks.py
3. (if you have not installed shadowsocks) sudo apt install shadowsocks-libev
4. ss-local -c ~/shadowsocks-parser/ss_config_{CONFIG NUMBER}.json
5. Open gnome settings->network Proxy, change socks host url to 127.0.0.1, and socks host port to 1080. Change ignore hosts to localhost, 127.0.0.0/8, ::1
6. Enjoy!