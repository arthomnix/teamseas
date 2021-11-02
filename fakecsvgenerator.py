import csv
import time

for i in range(5000):
    data = [int(time.time()+(60*i)), 500*i]
    with open('teamseas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
