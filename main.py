import json
from datetime import datetime


BASE_EMISSION = 251
FUEL_ADJUSTMENT = {"Petrol": 1.0, "Diesel": 1.15, "EV": 0.0}
TRAFFIC_ADJUSTMENT = {"Light": 1.0, "Moderate": 1.1, "Heavy": 1.2}

FILE_NAME = "trips.json"


def calculate_co2_savings(distance, fuel_type, traffic, idle_time, num_riders, travel_time):
    idle_emissions = 10 * idle_time
    nighttime_adjustment = 0.95 if travel_time >= 20 or travel_time < 6 else 1.0
    
    co2_savings = (
        distance
        * BASE_EMISSION
        * FUEL_ADJUSTMENT[fuel_type]
        * TRAFFIC_ADJUSTMENT[traffic]
        * nighttime_adjustment
        * (1 - 1 / num_riders)
        + idle_emissions
    )
    return round(co2_savings, 2)

def save_trip(data, file=FILE_NAME):
    try:
        with open(file, "r") as f:
            trips = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        trips = []
    
    trips.append(data)
    with open(file, "w") as f:
        json.dump(trips, f, indent=4)

def load_trips(file=FILE_NAME):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def display_summary(trips):
    if not trips:
        print("\nNo trips recorded yet.")
        return
    
    total_savings = sum(trip["CO2 Savings"] for trip in trips)
    print("\nCumulative Savings Summary:")
    print(f"Total CO2 Savings: {round(total_savings, 2)} grams")
    print(f"Total Trips Recorded: {len(trips)}\n")
    for i, trip in enumerate(trips, start=1):
        print(f"Trip {i}: {trip}")


def main():
    while True:
        print("\n--- Carbon Footprint Tracker ---")
        print("1. Record a new trip")
        print("2. View cumulative savings")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            try:
                distance = float(input("Enter trip distance (km): ").strip())
                fuel_type = input("Enter fuel type (Petrol, Diesel, EV): ").strip().capitalize()
                if fuel_type not in FUEL_ADJUSTMENT:
                    raise ValueError("Invalid fuel type")
                traffic = input("Enter traffic condition (Light, Moderate, Heavy): ").strip().capitalize()
                if traffic not in TRAFFIC_ADJUSTMENT:
                    raise ValueError("Invalid traffic condition")
                idle_time = int(input("Enter idle time (minutes): ").strip())
                num_riders = int(input("Enter number of riders: ").strip())
                if num_riders <= 0:
                    raise ValueError("Number of riders must be greater than 0")
                travel_time = int(input("Enter travel time (hour, 0-23): ").strip())
                if travel_time < 0 or travel_time > 23:
                    raise ValueError("Invalid travel time")
            except ValueError as e:
                print(f"Error: {e}")
                continue
            
            co2_savings = calculate_co2_savings(distance, fuel_type, traffic, idle_time, num_riders, travel_time)
            
            trip_data = {
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Distance (km)": distance,
                "Fuel Type": fuel_type,
                "Traffic Condition": traffic,
                "Idle Time (min)": idle_time,
                "Number of Riders": num_riders,
                "Travel Time (hour)": travel_time,
                "CO2 Savings": co2_savings,
            }
            save_trip(trip_data)
            print(f"\nTrip recorded! CO2 Savings: {co2_savings} grams")
        
        elif choice == "2":
            trips = load_trips()
            display_summary(trips)
        
        elif choice == "3":
            print("\nExiting. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
