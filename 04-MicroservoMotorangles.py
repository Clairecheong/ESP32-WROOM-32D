from machine import Pin, PWM

# Function to map angle to duty cycle
def angle_to_duty(angle):
    return int((angle / 180) * 115 + 20)

# Create PWM object for servo
servo = PWM(Pin(4), freq=50)

# Generate and print angles and duty cycles
angles = list(range(0, 181, 10))  # Angles from 0 to 180 in steps of 10
duty_cycles = [angle_to_duty(angle) for angle in angles]

for angle, duty_cycle in zip(angles, duty_cycles):
    print(f"Angle: {angle} degrees, Duty Cycle: {duty_cycle}")

# print
# Angle: 0 degrees, Duty Cycle: 20
# Angle: 10 degrees, Duty Cycle: 26
# Angle: 20 degrees, Duty Cycle: 32
# Angle: 30 degrees, Duty Cycle: 39
# Angle: 40 degrees, Duty Cycle: 45
# Angle: 50 degrees, Duty Cycle: 51
# Angle: 60 degrees, Duty Cycle: 58
# Angle: 70 degrees, Duty Cycle: 64
# Angle: 80 degrees, Duty Cycle: 71
# Angle: 90 degrees, Duty Cycle: 77
# Angle: 100 degrees, Duty Cycle: 83
# Angle: 110 degrees, Duty Cycle: 90
# Angle: 120 degrees, Duty Cycle: 96
# Angle: 130 degrees, Duty Cycle: 103
# Angle: 140 degrees, Duty Cycle: 109
# Angle: 150 degrees, Duty Cycle: 115
# Angle: 160 degrees, Duty Cycle: 122
# Angle: 170 degrees, Duty Cycle: 128
# Angle: 180 degrees, Duty Cycle: 135