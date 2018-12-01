
# test input
test_input = "+1, -1"
input = test_input.split(", ")

# Real input
with open("input.txt") as file:
    input = file.read().split("\n")

# Solution 1
frequency = 0
for value in input:
    frequency += int(value)

print('Frequency: {}'.format(frequency))

# Solution 2
orig = input
for i in range(500):
    input = input + orig

frequency = 0
history = [0]

for value in input:
    frequency += int(value)

    if frequency in history:
        print('Frequency {} reached twice.'.format(frequency))
        break

    history.append(frequency)

