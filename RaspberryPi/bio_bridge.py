import serial
import rtmidi
import time

PORT_SERIE = '/dev/ttyUSB0'
BAUD_RATE = 115200

midiout = rtmidi.MidiOut()
midiout.open_virtual_port("Bio-Arduino-Midi")

ser = serial.Serial(PORT_SERIE, BAUD_RATE, timeout=1)

buffer = bytearray() # tampon data reçue du port serie
message_affiche = False  # temoins affichage

while True:
    # lecture data port serie
    data = ser.read(1)
    if data:
        buffer += data

        if not message_affiche:
            print(f"Système 100% focntionnel !, Données reçues sur {PORT_SERIE}")
            message_affiche = True

    # attendre message complet MIDI (3 bytes)
    while len(buffer) >= 3:
        msg = buffer[:3]
        buffer = buffer[3:]

        status, note, vel = msg[0], msg[1], msg[2]

        # envoie message on off
        if status & 0xF0 in [0x80, 0x90]: # note off ou note on ok
            midiout.send_message([status, note, vel])
