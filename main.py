import random

# Define a list of possible mineral types.
mineral_types = ["Phosphorous", "Zinc", "Copper"]

# Function to simulate GPS coordinates and detected minerals along a route.
def simulate_gps_coordinates_between_points(start_point, end_point, num_points):
    start_latitude, start_longitude, _ = start_point
    end_latitude, end_longitude, _ = end_point
    gps_coordinates = []
    minerals_detected = []

    for i in range(num_points):
        latitude = start_latitude + (end_latitude - start_latitude) * i / (num_points - 1)
        longitude = start_longitude + (end_longitude - start_longitude) * i / (num_points - 1)
        detected_mineral = random.choice(mineral_types)
        gps_coordinates.append((latitude, longitude))
        minerals_detected.append(detected_mineral)

    return gps_coordinates, minerals_detected

# Get starting point information from the user.
start_place = input("Enter the name of the starting place: ")
start_latitude = float(input(f"Enter the latitude for {start_place}: "))
start_longitude = float(input(f"Enter the longitude for {start_place}: "))

# Get ending point information from the user.
end_place = input("Enter the name of the ending place: ")
end_latitude = float(input(f"Enter the latitude for {end_place}: "))
end_longitude = float(input(f"Enter the longitude for {end_place}: "))

# Define the number of points along the route.
num_points = int(input("Enter the number of points along the route: "))

# Create tuples for the starting and ending points.
start_point = (start_latitude, start_longitude, start_place)
end_point = (end_latitude, end_longitude, end_place)

# Collect latitude and longitude for additional points.
points = []
for i in range(num_points):
    point_name = input(f"Enter the name for point {i+1}: ")
    point_latitude = float(input(f"Enter the latitude for {point_name}: "))
    point_longitude = float(input(f"Enter the longitude for {point_name}: "))
    points.append((point_latitude, point_longitude, point_name))

# Call the function to simulate GPS coordinates and detected minerals along the route.
gps_coordinates_start, minerals_detected_start = simulate_gps_coordinates_between_points(start_point, points[0], num_points)
gps_coordinates_end, minerals_detected_end = simulate_gps_coordinates_between_points(points[-1], end_point, num_points)

print("\n")
# Combine GPS coordinates and detected minerals.
gps_coordinates = gps_coordinates_start[:-1] + gps_coordinates_end
minerals_detected = minerals_detected_start[:-1] + minerals_detected_end

print("\n")
# Print the results.
print(f"GPS Coordinates and Detected Minerals along the route from {start_place} to {end_place}:")
for i, (latitude, longitude) in enumerate(gps_coordinates, start=1):
    detected_mineral = minerals_detected[i - 1]
    print(f"Point {i}: Latitude {latitude}, Longitude {longitude} - Mineral: {detected_mineral}")

print("\n")
print("===============================================")
print("\n")
init_conc = float(input("Enter initial phosphorus concentration (mg/L): "))
acceptable_conc = 0.1  # Acceptable phosphorus concentration in mg/L

# Checking if the initial phosphorus concentration is already within acceptable limits
if init_conc <= acceptable_conc:
    print("Water is already within acceptable phosphorus limits. No purification needed.")
else:
    if 2.3 <= init_conc <= 157:
        print("Perform Ion Exchange Chromatography")
    elif 158 <= init_conc >= 163:
        print("Perform Precipitation and Filtration")
    elif 0.74 <= init_conc <= 2.2:
        print("Perform Dialysis")

print("\n")
print("===============================================")
print("\n")
# Function for cost
def cost():
    print("PHOSPHORUS")
    print("""Cost per kg: 100-120
    Available industries that will buy: Fertilisers, Animal Feeds, Rust
    Removers, Corrosion Preventers and Even Dishwasher Tablets
    States that require PHOSPHORUS: Uttar Pradesh, Punjab, Haryana, and Madhya Pradesh 
    """)

cost()
   