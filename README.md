# Multi-Camera Dashboard

## Materials and Equipment
### Software
|Software|Installation Link|
|--------|------|
|Arduino IDE|https://www.arduino.cc/en/software/|
|Visual Studio Code|https://code.visualstudio.com/|
### Components
|Component|Function|Notes|
|---------|---------|----|
|ESP32-S3-WROOM-1-N16R8|Microcontroller|16MB Flash + 8MB PSRAM|
|OV3660|Camera||

# Configuration

USB-UART
[Freenove](https://docs.freenove.com/projects/fnk0085/en/latest/)

## Setup
1. Connect the computer to the USB-UART port of the microcontroller.
2. Click <kbd>Win</kbd>, then search for 'Device Manager'. Open the program.
3. Under Ports (COM & LPT), check if the newly connected device is being recognized properly. It should be presented as `USB-Enhances-SERIAL 
CH343 (COMx)`. If not, head to [WinChipHead (WCH) then search for **CH343**](http://www.wch-ic.com/search?t=all&q=ch343).
4. Download the appropriate driver for your operating system. For Windows, download **CH343SER.EXE**.
5. Run the executable (i.e., CH343SER.EXE). In the DriverSetup window, click `Install`.
6. After installation, close the DriverSetup window.
