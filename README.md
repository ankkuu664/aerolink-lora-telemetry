AeroLink 

LoRa-Based Wireless Telemetry and Remote Command System

AeroLink is an embedded systems project built using the Raspberry Pi Pico (RP2040), SX1262 LoRa transceiver, and an OLED display. The project focuses on wireless telemetry reception, signal-strength monitoring, and sending remote commands between embedded devices.
I built this project to get hands-on experience with microcontrollers, LoRa communication, sensor-data handling, and hardware interfacing using MicroPython.
The system receives wireless messages, displays selected telemetry information on an OLED screen, and sends a Stop command when a physical trigger switch is activated.

Features

Wireless communication using the SX1262 LoRa transceiver.
Telemetry reception and packet monitoring.
RSSI measurement to monitor received signal strength.
OLED display for viewing system status and telemetry values.
Physical trigger switch for sending a Stop command.
RGB LED indicators for visual feedback.
MicroPython firmware running on the Raspberry Pi Pico.
Modular radio and display drivers.

Hardware Components
1. Raspberry Pi Pico (RP2040)
Purpose: Main microcontroller.
2. SX1262 LoRa Module
Purpose: Wireless communication.
3. SSD1306 OLED Display
Purpose: Displaying received information.
4. Trigger Switch
Purpose: Initiating the stop command.
5. RGB LEDs
Purpose: Visual status indication.
6. Jumper Wires and Power Supply
Purpose: Hardware connections.

Technologies Used
MicroPython
Raspberry Pi Pico
SX1262 LoRa
SPI and I²C communication
GPIO and PWM
Thonny IDE

Working
The Raspberry Pi Pico initializes the LoRa transceiver and OLED display before entering its main loop.
When a wireless message is received, the program reads the payload, obtains the RSSI value, updates the OLED display, and increments the received-packet counter. Battery information and the transmitter packet count are extracted from specific fields in the received message.
The trigger switch provides another way to interact with the system. When activated, the Pico sends a Stop message through the LoRa transceiver.
This project brings together wireless communication, hardware inputs, display interfacing, and embedded programming in a single system.

System Architecture        
 Wireless Transmitter
        |
     LoRa Link
        |
  SX1262 Transceiver
        |
      SPI
        |
  Raspberry Pi Pico
      (RP2040)
        |
        
-------------------------
|       |       |
I²C    GPIO    PWM
  |      |       |
OLED   Switch  RGB LEDs
  |
Telemetry Display


Command Path:
Trigger Switch - Pico - SX1262
                   |
                LoRa Link
                   |
             Remote Receiver

Project Structure

aerolink-lora-telemetry
── main.py
── receive_only.py
── sx1262.py
── sx126x.py
── _sx126x.py
── ssd1306.py
── ssd1305.py

Project Files
1. main.py
Main application for telemetry reception, display updates, and stop-command transmission.
2. receive_only.py
Basic receiver program for testing message reception and RSSI.
3. sx1262.py
SX1262-specific radio driver.
4. sx126x.py
Shared SX126x driver implementation.
5. _sx126x.py
Low-level radio commands, constants, and register definitions.
6. ssd1306.py
OLED display driver.
7. ssd1305.py
Additional OLED driver.

Pin Connections
SX1262 LoRa Module
Signal     	Raspberry Pi Pico GPIO
SCK	GP10
MOSI	GP11
MISO	GP12
CS	GP13
IRQ	GP14
RESET	GP15
GPIO/BUSY	GP16
OLED Display

Signal	Raspberry Pi Pico GPIO
SDA	GP0
SCL	GP1

Trigger Switch and LEDs
Component	Raspberry Pi Pico GPIO
Trigger switch	GP2
Red LED	GP8
Green LED	GP7
Blue LED	GP9
Onboard LED	GP25

LoRa Configuration
Parameter	  Value
Frequency	  868 MHz
Bandwidth	  250 kHz
Spreading factor	  12
Coding rate argument	  5
Sync word	  0x12
Transmit power	 22 dBm
Preamble length	  8
CRC	 Enabled
Header mode	 Explicit

Getting Started
Requirements
Raspberry Pi Pico (RP2040)
Compatible SX1262 LoRa module
SSD1306 OLED display
MicroPython firmware
Thonny IDE

Setup
Install Thonny IDE.
Install compatible MicroPython firmware on the Pico.
Connect the SX1262 module, OLED display, switch, and LEDs.
Upload main.py, sx1262.py, sx126x.py, _sx126x.py, and ssd1306.py to the Pico.
Open main.py in Thonny and run it.
Use a compatible LoRa transmitter to send test messages.

Current Limitations
The current implementation focuses on basic telemetry reception, RSSI monitoring, OLED updates, and stop-command transmission. Reliable command delivery, acknowledgements, authentication, and fail-safe behavior require additional development and testing.

The project is an experimental embedded communication system, not a safety-certified emergency-stop or flight-control system.

Conclusion
AeroLink is a practical project through which I explored wireless telemetry and embedded hardware integration. It combines a Raspberry Pi Pico, LoRa communication, an OLED display, and a physical input to create a compact monitoring and command system.
