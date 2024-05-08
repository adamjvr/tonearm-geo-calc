import math

def calculate_tonearm_geometry():
    print("Welcome to Turntable Tonearm Geometry Calculator!")
    print("Please enter the following dimensional parameters in millimeters:")

    pivot_to_stylus = float(input("Distance from pivot to stylus: "))
    effective_length = float(input("Effective length of the tonearm: "))
    overhang = float(input("Overhang distance (if any): "))
    mounting_distance = float(input("Mounting distance (distance from pivot to mounting hole): "))
    
    # Calculate offset angle
    offset_angle = math.degrees(math.atan((pivot_to_stylus - overhang) / effective_length))

    # Calculate null point distance
    null_point_distance = mounting_distance - (pivot_to_stylus - overhang)

    print("\nResults:")
    print("Offset Angle: {:.2f} degrees".format(offset_angle))
    print("Null Point Distance: {:.2f} mm".format(null_point_distance))

if __name__ == "__main__":
    calculate_tonearm_geometry()
