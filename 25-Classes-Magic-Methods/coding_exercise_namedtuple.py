# Use the namedtuple function to create a GymExercise class whose instances
# will have three attributes: name, weight, and reps.

# Assign a squat variable to a GymExercise tuple object with
# a name of “squat”, a weight of 265, and a rep count of 3.

# Assign a bench variable to a GymExercise tuple object with
# a name of “benchpress”, a weight of 185, and a rep count of 5.

# Assign a deadlift variable to a GymExercise tuple object with
# a name of “deadlift”, a weight of 225, and a rep count of 6.

# Assign a press variable to a GymExercise tuple object with
# a name of “press”, a weight of 120, and a rep count of 8.
import collections

GymExercise = collections.namedtuple("GymExercise", ["name", "weight", "reps"])

squat = GymExercise("squat", 265, 3)
print(squat.name)
print(squat.weight)
print(squat.reps)

bench = GymExercise(name="benchpress", weight=185, reps=5)
print(bench.name)
print(bench.weight)
print(bench.reps)

deadlift = GymExercise("deadlift", 225, 6)
print(deadlift.name)
print(deadlift.weight)
print(deadlift.reps)

press = GymExercise("press", 120, 8)
print(press.name)
print(press.weight)
print(press.reps)
