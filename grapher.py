# Team Seas graph generator

import csv
import matplotlib.pyplot as plot
from matplotlib.ticker import FuncFormatter
import datetime


# number formatters

integer = lambda i, p: "$%i" % i
intformatter = FuncFormatter(integer)

date = lambda i, p: datetime.datetime.utcfromtimestamp(i).strftime("%Y-%m-%d %H:%M:%S")
dateformatter = FuncFormatter(date)

# read the csv file into a list
# this list is in the format [[time, donations], [time, donations], ...]

with open('teamseas.csv', 'r', newline='') as file:
    data = list(csv.reader(file))


# convert the list into two lists, one for timestamps and one for donations

timestamps = [int(list[0]) for list in data]
donations = [int(list[1]) for list in data]

fig, ax = plot.subplots()
# plot the data
ax.plot(timestamps, donations, color="#2AA198")
# set formatters
ax.yaxis.set_major_formatter(intformatter)
ax.xaxis.set_major_formatter(dateformatter)
# set number of ticks on each axis
ax.locator_params(axis='x', nbins=30)
ax.locator_params(axis='y', nbins=20)
# set labels and graph title
ax.set(xlabel="Time (UTC)", ylabel="Total donations (USD)", title="Team Seas Donations")
# set colours (solarized dark pog)
# colour of title
ax.title.set_color("#268BD2")
# colour of axis labels
ax.xaxis.label.set_color("#859900")
ax.yaxis.label.set_color("#859900")
# colour of spines (graph borders)
for spine in ax.spines.values(): spine.set_edgecolor("#586E75")
# colour of tick labels
# also rotate the time by 90 degrees
ax.tick_params(axis='x', labelrotation=90, colors="#268BD2")
ax.tick_params(axis='y', colors="#268BD2")
# background colour of just the graph
ax.set_facecolor(color="#002B36")
# background colour of the whole image
fig.set_facecolor(color="#073642")
# colour of grid lines
ax.grid(color="#586E75")
# add padding on the bottom so the timestamps don't get cut off
fig.subplots_adjust(bottom=0.2)

# save plot to an image
fig.savefig("plot.png", bbox_inches='tight', dpi=300)
