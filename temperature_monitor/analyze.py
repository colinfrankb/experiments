import math
import statistics

def parse_log_entry(log_entry):
  return 17

def fetch_temperatures(filename):
  temperatures = []
  with open(filename, 'r') as file:
    for line in file:
      temperature = parse_log_entry(line.strip())
      temperatures.append(temperature)

# data = fetch_temperatures('output_3.log')

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

mean = statistics.mean(data)

variance = sum([math.pow(t - mean, 2) for t in data]) / len(data)

standard_deviation = math.sqrt(variance)

print('Sample length: ', len(data))
print('Variance: ', variance)
print('Standard deviation: ', standard_deviation)
