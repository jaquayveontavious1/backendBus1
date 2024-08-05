import random

initial_bus_location = [
    {'bus_number':1,"latitude":-1.2921,"longitude": 36.8219}
]
def update_bus_location(bus_locations) :
    for bus in bus_locations :
        bus['latitude'] +=random.uniform(-0.001,0.001)
        bus['longitude'] += random.uniform(-0.001,0.001)
        return bus_locations