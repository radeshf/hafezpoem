import csv
import random
import pkgutil
from io import StringIO

def get_random_fal():
    csv_data = pkgutil.get_data(__name__, 'poems.csv').decode('utf8')
    csv_reader = csv.reader(StringIO(csv_data), delimiter=',')
    line_count = 0
    rnd = random.randrange(0, 495)
    for row in csv_reader:
        if rnd == line_count:
            return row[2]
        line_count += 1
