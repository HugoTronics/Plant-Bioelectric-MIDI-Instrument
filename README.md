# Turning a Plant's Electrical Signals Into Music: A Bio-Sonification Build

<p align="center">
    <img src="https://img.shields.io/badge/platform-Arduino-%2300979d.svg?style=for-the-badge&logo=arduino" alt="Arduino">
    <img src="https://img.shields.io/badge/platform-Raspberry%20Pi-%23a22846.svg?style=for-the-badge&logo=raspberrypi" alt="Raspberry Pi">
    <img src="https://img.shields.io/badge/language-Python-blue.svg?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/protocol-MIDI-yellow.svg?style=for-the-badge&logo=midi" alt="MIDI">
</p>

## :open_book: Project Overview

This repository contains the resources for a bio-sonification instrument: a system that captures the faint bioelectric signals of a houseplant and converts them into real-time MIDI music. It covers the full signal chain — analog acquisition, an Arduino-based processing stage, and a Raspberry Pi sound engine — from circuit design to a working, headless installation.

### Features

- **Analog Front-End**: Op-amp based acquisition circuit (CA3140) with low-pass filtering for clean bioelectric signal capture.
- **Arduino Signal Processing**: Real-time sampling, digital smoothing, and threshold-based MIDI note/chord generation.
- **Raspberry Pi Sound Engine**: Python MIDI bridge feeding a SunVox-based synthesizer for continuous, evolving sound.
- **Autostart Setup**: Scripts for a fully headless installation that starts on boot.

<!-- Replace this with your demo video, uploaded via a GitHub issue (drag & drop), then paste the resulting https://github.com/user-attachments/... link here -->
**demo.mp4**

https://github.com/user-attachments/assets/REPLACE-WITH-YOUR-VIDEO-ID

## :link: Explore the Full Project

For a detailed walkthrough of the project, including the analog design, signal processing algorithm, and testing results, check out the full article:

<p align="center">
    <a href="https://hugotronics.github.io/turning-a-plants-electrical-signals-into-music-a-bio-sonification-build/" target="_blank">
        <img src="https://img.shields.io/badge/Read%20the%20Full%20Article-%230084ff.svg?style=for-the-badge&logo=read-the-docs" alt="Read the Full Article">
    </a>
</p>

This article includes:

- **Signal Characterization**: Understanding plant bioelectric activity and the noise challenges around it.
- **Circuit Design**: The full analog front-end, gain and filter calculations.
- **Firmware Walkthrough**: How raw sensor readings become MIDI chords and melody.
- **Results and Testing**: Filter performance, noise rejection, and sensor validation.

## :rocket: Getting Started

### Files Included

1. **Arduino**:
    - `Arduino/code_arduino_2_capteurs`: Main firmware — signal acquisition, filtering, and MIDI generation for two sensor channels.
    - `Arduino/detect_manu`: Standalone test sketch for validating raw sensor readings before running the full system.

2. **Raspberry Pi**:
    - `RaspberryPi/bio_bridge.py`: Python script that bridges Arduino serial MIDI messages to a virtual MIDI port.
    - `RaspberryPi/start_bio_instrument.sh`: Startup script that launches SunVox and the MIDI bridge.
    - `RaspberryPi/bio_instrument.desktop`: Autostart entry for headless boot-time launch.

3. **Documentation**:
    - `Documentation/hardware_list.txt`: Full bill of materials.
    - `Documentation/setup_guide.txt`: Step-by-step installation and configuration guide, including troubleshooting.
    - `Documentation/schematics/`: Circuit schematics, Arduino pinout, and component datasheets.

### How to Use

1. **Download the Files**:
   - Clone this repository or download the files directly from the [GitHub repository](https://github.com/HugoTronics/Plant-Bioelectric-MIDI-Instrument).

2. **Build the Acquisition Circuit**:
   - Follow the schematics in `Documentation/schematics/` to assemble the analog front-end on a breadboard.

3. **Flash the Arduino**:
   - Open `Arduino/code_arduino_2_capteurs` in the Arduino IDE and upload it to an Arduino Nano (or compatible board).

4. **Set Up the Raspberry Pi**:
   - Install SunVox and Python dependencies (`pyserial`, `python-rtmidi`), then run `RaspberryPi/bio_bridge.py`.

## :hammer_and_wrench: Installation and Setup

1. **Circuit Assembly**:
   - Wire the CA3140-based acquisition stage as shown in the schematics, one channel per plant sensor.

2. **Firmware Upload**:
   - Flash the Arduino with the provided sketch and verify sensor readings via the Serial Monitor.

3. **Software Setup**:
   - Install SunVox on the Raspberry Pi, configure the virtual MIDI port, and enable autostart using the provided `.desktop` and `.sh` files.

## :test_tube: Testing and Validation

1. **Sensor Validation**:
   - Verify that contact with a plant produces a measurable, variable signal on the Arduino's Serial Monitor.

2. **Filter Validation**:
   - Inject test signals at different frequencies to confirm the low-pass filter rejects mains-frequency noise while preserving the biological signal band.

3. **Full System Test**:
   - Confirm MIDI messages reach SunVox and trigger audible notes in response to plant activity.

## :memo: Documentation and References

- **SunVox**: Lightweight modular synthesizer used for sound generation — [warmplace.ru/soft/sunvox](https://warmplace.ru/soft/sunvox/)
- **python-rtmidi**: Python MIDI I/O library (MIT license)
- **pyserial**: Python serial communication library (BSD-3-Clause license)

## :wrench: Future Improvements

- Move from breadboard to a custom PCB.
- Improve sensor design and long-term contact reliability.
- Add more simultaneous plant channels for a larger "plant orchestra."
- Battery-powered, fully portable enclosure.

## :mailbox: Contact and Support

For questions or support, please open an issue on this GitHub repository or contact [corsahu@gmail.com](mailto:corsahu@gmail.com).

## :book: Additional Resources

- [SunVox](https://warmplace.ru/soft/sunvox/)
- [Arduino IDE](https://docs.arduino.cc/software/ide/)
- [CA3140 Datasheet](https://www.ti.com/product/CA3140)

---
