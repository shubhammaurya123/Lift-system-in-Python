# Number of lifts in the building
n = 2

# Number of floors in the building
m = 10

# Initialize the current floors and states of the lifts
lifts = [(0, "close") for _ in range(n)]

# Function to update the state of a lift
def update_lift_state(lift, state):
    lifts[lift] = (lifts[lift][0], state)

# Function to move a lift to a new floor
def move_lift(lift, new_floor):
    # Calculate the time required to reach the new floor
    time_required = abs(lifts[lift][0] - new_floor)
    # Update the current floor of the lift
    lifts[lift] = (new_floor, lifts[lift][1])
    return time_required

# Function to open or close a lift
def change_lift_state(lift):
    if lifts[lift][1] == "close":
        update_lift_state(lift, "open")
    else:
        update_lift_state(lift, "close")

# Function to handle a lift request
def handle_request(start, destination):
    # Find the nearest lift
    nearest_lift = min(lifts, key=lambda x: abs(x[0] - start))
    # Move the lift to the start floor
    time_taken = move_lift(nearest_lift, start)
    # Open the lift
    change_lift_state(nearest_lift)
    # Wait for the person to enter
    time_taken += 1
    # Close the lift
    change_lift_state(nearest_lift)
    # Move the lift to the destination floor
    time_taken += move_lift(nearest_lift, destination)
    # Open the lift
    change_lift_state(nearest_lift)
    # Wait for the person to exit
    time_taken += 1
    # Close the lift
    change_lift_state(nearest_lift)
    return time_taken

# Function to display the current state of the lifts
def display_lifts():
    for i, lift in enumerate(lifts):
        print(f"LIFT {i+1}: {lift[0]} ({lift[1]})")

# Initialize the time to 0
time = 0

# First request: lift from 0th floor to the 7th floor
print(f"T={time}")
display_lifts()
time += handle_request(0, 7)

# Second request: lift from 3rd floor to the 0th floor
print(f"T={time}")
display_lifts()
time += handle_request(3, 0)

# Third request: lift from 4th floor to the 6th floor
print(f"T={time}")
display_lifts()
time += handle_request(4, 6)

print(f"Total time taken: {time} seconds")
