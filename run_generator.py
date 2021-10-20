curl -fsSL https://code-server.dev/install.sh | sh > /dev/null
npm install -g localtunnel > /dev/null
sudo apt-get install screen &> /dev/null
print('\n')
code-server --bind-addr 127.0.0.1:8888 --auth none & lt --port 8888
