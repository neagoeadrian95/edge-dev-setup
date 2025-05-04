#!/bin/bash

echo "Getting system updates..."
(sudo apt update || (((sudo dpkg --configure -a && sudo apt update) || apt --fix-broken install) && sudo apt update)) && sudo apt upgrade -y

echo "Install required packages..."
sudo apt install -y \
  git python3-pip python3-venv python3-opencv \
  docker.io docker-compose \
  mosquitto mosquitto-clients \
  htop i2c-tools build-essential cmake

echo "Creating "docker" group..."
sudo groupadd docker

echo "Add user to the docker group..."
sudo usermod -aG docker "$USER"

echo "Fetch and update Git submodules..."
git submodule update --init --recursive

echo "Updating user group..."
echo "Setup Complete"
newgrp docker


