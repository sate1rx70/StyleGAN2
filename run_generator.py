curl -fsSL https://code-server.dev/install.sh | sh
npm install -g localtunnel 
sudo apt-get install screen &
print('\n')
code-server --bind-addr 127.0.0.1:8888 --auth none & lt --port 8888
