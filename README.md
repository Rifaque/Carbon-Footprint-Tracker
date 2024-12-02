# Carbon Footprint Tracker

## Introduction
This is a command-line application for RideBuddy, designed to dynamically calculate and track carbon footprint savings for rideshare trips. The app uses real-world variables like fuel types, traffic patterns, trip durations, and idle time to calculate CO₂ emissions savings. It also stores trip data persistently, allowing users to review cumulative savings.

---

## Features
1. **CO₂ Savings Calculation**:
   - Dynamically calculates emissions based on:
     - Distance
     - Fuel type (Petrol, Diesel, EV)
     - Traffic condition (Light, Moderate, Heavy)
     - Idle time
     - Number of riders
     - Travel time (nighttime adjustment)
   
2. **Persistent Storage**:
   - Saves trip data to a JSON file for future reference.

3. **Cumulative Savings**:
   - Displays a summary of all recorded trips, including total CO₂ savings and trip details.

4. **User-Friendly Interface**:
   - Menu-driven command-line interface.

---

## Installation and Requirements

### Requirements
- Python 3.7 or higher

### Installation
1. Clone the repository or download the source code.
2. Ensure Python is installed on your system.
3. No additional libraries are required (uses Python's built-in modules).

---

## How to Use

1. **Run the program**:
   - Open your terminal or command prompt and navigate to the directory where the `carbon_tracker.py` file is located.
   - Run the following command to start the application:
     ```bash
     python carbon_tracker.py
     ```

2. **Follow the menu options**:
   The application will display a menu with the following options:
   
   - **Option 1: Record a New Trip**  
     This option will prompt you to enter details about a trip. The following inputs are required:
     - **Distance**: Enter the distance of the trip in kilometers (e.g., `15`).
     - **Fuel Type**: Choose the type of fuel used in the vehicle. Options include:
       - `Petrol`
       - `Diesel`
       - `EV`
     - **Traffic Condition**: Select the traffic condition during the trip. Options include:
       - `Light`
       - `Moderate`
       - `Heavy`
     - **Idle Time**: Enter the idle time (in minutes) during the trip (e.g., `5`).
     - **Number of Riders**: Enter the number of people riding in the vehicle (e.g., `3`).
     - **Travel Time**: Enter the time of the trip in 24-hour format (e.g., `21` for 9 PM).

     Once the details are entered, the program will calculate the CO₂ savings for the trip and display the result.

   - **Option 2: View Cumulative Savings**  
     This option will display a summary of all recorded trips, including the total CO₂ savings from all trips. It will also list each trip's details such as:
     - Date and time of the trip
     - Distance
     - Fuel type
     - Traffic condition
     - Idle time
     - Number of riders
     - CO₂ savings for each trip

   - **Option 3: Exit the Application**  
     Select this option to close the application.

3. **Persistent Data**:
   The program saves all trip data in a file named `trips.json`. This file is automatically created when a trip is recorded. The data in this file persists even if the program is closed, so you can view the cumulative savings across multiple sessions.

---

## Code Structure

- **Functions**:
  - `calculate_co2_savings`: This function computes the carbon footprint savings for a trip. It takes into account factors like distance, fuel type, traffic condition, idle time, and the number of riders.
  - `save_trip`: This function saves the trip data to a JSON file (`trips.json`) after each trip is recorded.
  - `load_trips`: This function loads all recorded trips from the `trips.json` file to allow for cumulative savings and display of trip data.
  - `display_summary`: This function displays the cumulative savings for all recorded trips, including individual trip details.

- **Files**:
  - `carbon_tracker.py`: The main Python program file that handles the logic of recording trips, calculating CO₂ savings, and displaying results.
  - `trips.json`: A JSON file used to store trip data persistently. This file is automatically created when the first trip is recorded and is updated with each new trip.

---

## License
This project is open-source and can be used or modified freely under the MIT License.

---

## Contact
For questions or suggestions, please reach out to [rifaque123@gmail.com](mailto:rifaque123@gmail.com).
