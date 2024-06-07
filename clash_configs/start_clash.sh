mkdir -p ~/.clash
# ln -s ./clash_configs/config.yaml ~/.clash/config.yaml
# ln -s ./clash_configs/gcp.yaml ~/.clash/gcp.yaml
# ln -s ./clash_configs/Country.mmdb ~/.clash/Country.mmdb
chmod +x ./clash-linux-amd64-v3
./clash-linux-amd64-v3 -f clash_configs/gcp.yml