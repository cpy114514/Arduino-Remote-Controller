# Import the library for serial communication (Arduino to PC)
import serial

# Import the library to simulate keyboard inputs
import pyautogui

# Open the serial port (make sure 'COM3' matches your Arduino port)
# 9600 is the baud rate – it must match Serial.begin(9600) in your Arduino code
ser = serial.Serial('COM3', 9600)

# Infinite loop to keep listening for incoming data from Arduino
while True:
    # If there is data waiting in the serial buffer
    if ser.in_waiting:
        # Read a line from the serial port, decode it to string, and clean up any extra characters
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        # If the received line is the IR code for button "2"
        if line == "Received IR code: 0xE718FF00":
            # Simulate pressing Alt + F4 (close current window)
            pyautogui.hotkey('alt', 'f4')

        # If the received line is the IR code for button "1"
        if line == "Received IR code: 0xF30CFF00":
            # Simulate pressing the letter 'a'
            pyautogui.press('a')
