from collections import defaultdict
from functools import reduce

output = defaultdict(lambda: defaultdict(dict))

items = [
    {'category': 'Mon', 'name': 'female', 'value': 42}, 
    {'category': 'Mon', 'name': 'male', 'value': 24},
    {'category': 'Tues', 'name': 'male', 'value': 12},
    {'category': 'Tues', 'name': 'female', 'value': 13},
    {'category': 'Wed', 'name': 'male', 'value': 15},
    {'category': 'Wed', 'name': 'female', 'value': 26},
]

for item in items:
    output[item['category']][item['name']] = item['value']


result = defaultdict(lambda: dict)

print(dict(output))
