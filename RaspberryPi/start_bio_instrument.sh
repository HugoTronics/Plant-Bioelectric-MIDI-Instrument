#!/bin/bash

echo "Démarrage du système"

# lance sunvox
/home/plante/Téléchargements/sunvox/sunvox/linux_arm64/sunvox &

# attendre demarrage snvox
sleep 5

# attendre port usb
while [ ! -e /dev/ttyACM0 ]
do
  echo "Attente du port USB"
  sleep 2
done

echo "Port USB ok"

# lance le bridge MIDI
lxterminal -e "python3 /home/plante/Téléchargements/bio_bridge.py"