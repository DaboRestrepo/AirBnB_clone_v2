#!/usr/bin/env bash
# Prepair the web servers
sudo apt update
sudo apt install nginx -y
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo '<!DOCTYPE html>
<html>
<head>
</head>
<body>
<p>I am an entry.</p>
</body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
