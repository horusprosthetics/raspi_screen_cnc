print("Door locked ")
d.setFloodState(FloodState.ON)

print("Homing axes ")
d.executeAxisHoming(Axis.Z)
d.executeAxisHoming(Axis.X)
d.executeAxisHoming(Axis.A)

print("Starting the milling process")
d.startTrajectory()