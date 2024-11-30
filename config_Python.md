sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13
python3.13 --version

Configurar la Versión Predeterminada
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1
sudo update-alternatives --config python3



