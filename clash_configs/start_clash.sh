# add the following to .bashrc
# export http_proxy=http://127.0.0.1:7890/
# export HTTP_PROXY=http://127.0.0.1:7890/
 # this has to be http, not https
# export https_proxy=http://127.0.0.1:7890/
# export HTTPS_PROXY=http://127.0.0.1:7890/
# export all_proxy=socks5://127.0.0.1:7891/
# export ALL_PROXY=socks5://127.0.0.1:7891/
chmod +x ./clash-linux-amd64-v3
./clash-linux-amd64-v3 -f clash_configs/gcp.yml
