import csv
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

total_km = 0.0
points = []

# Load coordinates from the exported CSV
with open('path.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        points.append((float(row['lat']), float(row['lon'])))

# Sum the distance between each point
for i in range(len(points) - 1):
    total_km += haversine(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

print(f"Total Travel Distance: {total_km:.2f} km")