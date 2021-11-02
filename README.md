# teamseas

This repository contains code for collecting, logging and graphing donations data from TeamSeas.

## teamseas.py
Dependencies: `requests`
`teamseas.py` gets the total donations every minute and logs it to a CSV file, `teamseas.csv`.
Each row of this file is in the format `time, donations` (`time` is the UNIX timestamp), with no column headers.

It also calculates the rate of change of donations per minute over the past hour, and extrapolates this to get an ***extremely bad*** prediction of when TeamSeas will hit $30 million.

## grapher.py
Dependencies: `matplotlib`
`grapher.py` reads data from `teamseas.csv` and generates a graph from it, which is saved to `plot.png`. Times are in UTC.
The graph uses the solarized dark colour scheme by default.

## fakecsvgenerator.py
Generates a fake `teamseas.csv` for testing purposes.
