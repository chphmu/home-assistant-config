# Readme FireTV

## Install Prereq
https://home-assistant.io/components/media_player.firetv/

## Create autostart
```bash
sudo nano /lib/systemd/system/firetv.service
sudo chmod 644 /lib/systemd/system/firetv.service 
sudo systemctl daemon-reload 
sudo systemctl enable firetv.service
sudo reboot
```

See content in firetv.service file in repo
