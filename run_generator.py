ccurl -fsSL https://code-server.dev/install.sh | sh &> /dev/null
apt-get install screen &> /dev/null
apt-get install --yes git ssh python3-venv &> /dev/null
wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip -qq -n ngrok-stable-linux-amd64.zip
get_ipython().system_raw('./ngrok http 8888 &')
sleep 3
import requests
from re import sub
r = requests.get('http://localhost:4040/api/tunnels')
str_ssh = r.json()['tunnels'][0]['public_url']
print(str_ssh)
code-server --bind-addr 127.0.0.1:8888 --auth none &
