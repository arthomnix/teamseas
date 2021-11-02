# Team Seas scraper / data logger
import requests
import csv
import time
import datetime

# scraping team seas' api is remarkably simple
getTeamSeasDonations = lambda: int(requests.get("https://tscache.com/donation_total.json").json()["count"])

if __name__ == "__main__":
    rollingDonations = []
    while True:
        try:
            donations = getTeamSeasDonations()
            rollingDonations.append(donations)
            # make sure the length never gets above 60
            if len(rollingDonations) > 60:
                rollingDonations.pop(0)
            # don't try and calculate rate of change if there is only one item in the array
            if len(rollingDonations) > 1:
                rateOfChange = (rollingDonations[-1] - rollingDonations[0]) / (len(rollingDonations)-1)
                donationsUntilTarget = 30000000 - donations
                minutesToReachTarget = donationsUntilTarget / rateOfChange
                predictedTimeToReachTarget = time.time() + (60 * minutesToReachTarget)
                print("Rate of change: $%s per minute" % str(rateOfChange))
                print("Predicted time to reach $30 million: %s" % datetime.datetime.fromtimestamp(int(predictedTimeToReachTarget)).strftime('%Y-%m-%d %H:%M:%S'))
            # write timestamp and donations to csv file
            with open('teamseas.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                row = [int(time.time()), donations]
                print(row)
                writer.writerow(row)
            time.sleep(60)
        except KeyboardInterrupt:
            # i still want to be able to ctrl+c out of the program
            break
        except:
            # extremely good error handling that will never cause any problems whatsoever
            # wait for a bit to avoid spamming the api if it returns data we don't expect
            time.sleep(5)
