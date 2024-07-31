# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:38:42 2024

@author: User
"""

import csv
import pandas as pd

with open('D:/7150CEM/Data/bankruptcy/1year.arff', 'r') as arff_file, open('D:/7150CEM/FirstYear.csv', 'w', newline='') as csv_file:
    # Read the ARFF file line by line
    lines = arff_file.readlines()

    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row to the CSV file
    header = [x.split()[1] for x in lines if x.startswith('@attribute')]
    writer.writerow(header)

    # Write the data rows to the CSV file
    data_start = lines.index('@data\n') + 1
    for line in lines[data_start:]:
        row = line.strip().split(',')
        writer.writerow(row)
        

