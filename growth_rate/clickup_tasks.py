import argparse
import csv
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description='Process growth rate of tasks.')
parser.add_argument(
    'file',
    help='csv file that must contain Date Created'
)
args = parser.parse_args()

dates = []

with open(args.file) as csv_file:
  reader = csv.DictReader(csv_file)

  for row in reader:
    dates.append(datetime.strptime(row['Date Created'], '%Y-%m-%dT%H:%M:%S.%fZ').date())

dates.sort()

start_date = dates[0]
end_date = start_date + timedelta(days=7)
last_date = dates[-1]

counts = {}

while(start_date <= last_date):
    interval_count = 0

    for date in dates:
        if date >= start_date and date < end_date:
            interval_count += 1

    counts['{} <= x < {}'.format(start_date, end_date)] = interval_count

    start_date = end_date
    end_date = start_date + timedelta(days=7)

for k, v in counts.items():
    print(k, '=', v)
