# Since the ESP32-WROOM-32D on a fireBeetle has 10 touchpins. 
# --- Code ---
from machine import TouchPad, Pin

# Function to read and print touch values for all available touch pins
def read_touch_pins():
    for pin_num in range(10):
        touch_pin = TouchPad(Pin(pin_num))
        touch_value = touch_pin.read()
        #Call the function to read and print touch values
        print(f"Touch Pin T{pin_num}: {touch_value}")

# ----- For my board -----
# Touch Pin GPIO4: 635
# Error reading Touch Pin GPIO5: invalid pin for touchpad
# Error reading Touch Pin GPIO6: invalid pin for touchpad
# Error reading Touch Pin GPIO7: invalid pin for touchpad
# Error reading Touch Pin GPIO8: invalid pin for touchpad
# Error reading Touch Pin GPIO9: invalid pin for touchpad
# Error reading Touch Pin GPIO10: invalid pin for touchpad
# Error reading Touch Pin GPIO11: invalid pin for touchpad
# Touch Pin GPIO12: 596
# Touch Pin GPIO13: 727
# Touch Pin GPIO14: 654
# Touch Pin GPIO15: 654