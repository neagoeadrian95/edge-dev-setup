# edge-dev-setup

Linux environment for edge computing using OpenCV and MQTT.

## Setup development environment for Raspberry Pi 3B+

Using Raspberry Pi OS Lite 64-bit.

### ⚙️ Automated setup script

To automatically install and configure the environment:

```bash
git clone git clone https://github.com/neagoeadrian95/edge-dev-setup.git
cd edge-dev-setup
chmod +x setup.sh
./setup.sh
```

> The script installs all required packages, configures Docker permissions, and optionally enables remote MQTT access.

### 🔧 Install base packages

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
  git python3-pip python3-venv python3-opencv \
  docker.io docker-compose \
  mosquitto mosquitto-clients \
  htop i2c-tools build-essential cmake
```

### 📦 Package list and usage

| Package              | Role                                                                 |
|----------------------|----------------------------------------------------------------------|
| `git`                | Version control – sync code with GitHub                             |
| `python3-pip`        | Python package manager (for installing AI/ML libraries)             |
| `python3-venv`       | Create isolated Python virtual environments                         |
| `python3-opencv`     | Computer vision library (OpenCV)                                    |
| `docker.io`          | Run isolated containers (easy software delivery)                    |
| `docker-compose`     | Orchestrate multiple Docker containers                              |
| `mosquitto`          | Local MQTT broker – for IoT prototypes                              |
| `mosquitto-clients`  | CLI tools (`mosquitto_pub`, `mosquitto_sub`) for MQTT testing       |
| `htop`               | Advanced system resource monitor (CPU/RAM usage)                    |
| `i2c-tools`          | Scan and test I2C devices (sensors)                                 |
| `build-essential`    | Compiler toolchain (gcc, make etc.)                                 |
| `cmake`              | Cross-platform build system (used in many C++/AI projects)          |

### 🐳 Docker configuration

Add your user (`goe`) to the `docker` group to allow running containers without `sudo`:

```bash
sudo usermod -aG docker goe
```

Log out and back in, or run:

```bash
newgrp docker
```

Test Docker installation:

```bash
docker run hello-world
```

### 🧪 Test OpenCV with Python

```bash
python3
>>> import cv2
>>> print(cv2.__version__)
```

If the version prints correctly, OpenCV is working.

### 📡 Test local MQTT communication (Mosquitto)

You can test if the MQTT broker works locally using the Mosquitto CLI tools:

#### 1. Subscribe to a topic (in one terminal):

```bash
mosquitto_sub -t test
```

#### 2. Publish a message to the same topic (in another terminal):

```bash
mosquitto_pub -t test -m "Hello from Raspberry Pi"
```

If you see the message appear in the subscriber terminal, MQTT is working locally.

---

### 🌐 Allow remote MQTT access (optional)

By default, Mosquitto allows only local connections. To allow other devices in your network to connect:

#### 1. Create a config file:

```bash
sudo nano /etc/mosquitto/conf.d/default.conf
```

#### 2. Add the following content:

```
listener 1883
allow_anonymous true
```

> ⚠️ Warning: `allow_anonymous true` is insecure and should only be used for local testing.

#### 3. Restart the Mosquitto service:

```bash
sudo systemctl restart mosquitto
```

#### 4. Confirm it's listening on the network:

```bash
sudo ss -tulpn | grep 1883
```

Now other devices in your LAN can connect to your Pi's MQTT broker using its IP address and port `1883`.

---

### 🧰 Useful systemctl commands

These will help you manage background services like Mosquitto and Docker:

```bash
# Check if Mosquitto is running
sudo systemctl status mosquitto

# Restart Mosquitto after config changes
sudo systemctl restart mosquitto

# Enable Mosquitto to start automatically on boot
sudo systemctl enable mosquitto

# Stop Mosquitto if needed
sudo systemctl stop mosquitto
```
