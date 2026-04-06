### Selenium

1. requirements.txt (pip) → dependências Python do robô
2. pacotes do sistema (apt) → tudo que o Chromium precisa para rodar headless no Linux

# 📦 requirements.txt (Python)

Para o script que você usou, o mínimo necessário é:

```sh
selenium==4.40.0
webdriver-manager==4.0.2
python-dotenv==1.0.1
requests==2.32.3
```

# 🐧 Pacotes instalados via APT (Linux headless)

Esses são os que garantem que o Chromium headless funcione sem crash:

```sh
sudo apt update
sudo apt install -y \
  chromium \
  libnss3 \
  libxss1 \
  libgbm1 \
  libatk-bridge2.0-0 \
  libgtk-3-0 \
  libasound2 \
  fonts-liberation \
  xdg-utils \
  libu2f-udev \
  libvulkan1
```