def mru (velocity, time):
    if(velocity < 0 or time <0 ):
        return "Error"
    else:
        return velocity*time

def mruv2 (initial_velocity, time, acceleration):
    if(initial_velocity < 0 or time <0 or acceleration < 0):
        return "Error"
    else:
        return initial_velocity*time + (acceleration * time*time)/2

def mruv3 (initial_velocity, time, acceleration):
    if(initial_velocity < 0 or time <0 or acceleration < 0):
        return "Error"
    else:
        return (initial_velocity*time) + (acceleration * time*time)
