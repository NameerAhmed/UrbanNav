import math

# Functions related to battery management

def update_battery(state, soc):


    pass


if __name__ == '__main__':
    # Example usage

    E = 1 # total energy capacity
    reserve_thresh = 0.2
    max_hover_time = 15 # in minutes
    dt = 1 # time step in minutes

    state = {
        'takeoff': 1.0,
        'cruising': 0.3,
        'queueing': 0.2,
        'charging': 2.0
    }

