import os
import sys
import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, '')


# Generate a financial report to the output device given. It could be a file or the stdout (the terminal).

def generate_report(output_dev, report_dict):
    output_dev.write("Financial Analysis\n------------------ \n")
    output_dev.write("Total Months: " + str(report_dict["Total Months"]) + "\n")
    output_dev.write("Total: " + locale.currency(report_dict["Total"], grouping=True) + "\n")
    output_dev.write("Average Change: " + locale.currency(report_dict["Average Change"], grouping=True) + "\n")
    output_dev.write("Greatest Increase in Profits: " + report_dict["Max Increase"][0] + " (" + locale.currency(report_dict["Max Increase"][1], grouping=True) + ")\n")
    output_dev.write("Greatest Decrease in Profits: " + report_dict["Max Decrease"][0] + " (" + locale.currency(report_dict["Max Decrease"][1], grouping=True) + ")\n")

# get the data and load it into a data frame
my_dir = os.getcwd()
data_file = os.path.join(my_dir, "Resources/budget_data.csv")

bank_df = pd.read_csv(data_file, encoding="utf-8")


# create a monthly change column in the bank dataframe
# while we're looping, find max and min change information
delta = np.array([float("nan")])
delta_max = 0
delta_min = 0
#loop through the records. Skip the first row of data since there is no "previous" month to calculate from
for i in range(1,len(bank_df)):
    delta = np.append(delta, (bank_df["Profit/Losses"][i] - bank_df["Profit/Losses"][i-1]))
    if delta[i] > delta_max:
        delta_max = delta[i]
        month_max = bank_df["Date"][i]
    if delta[i] < delta_min:
        delta_min = delta[i]
        month_min = bank_df["Date"][i]
# add the change array as a column to the dataframe
bank_df["Monthly Change"] = delta.tolist()


# generate summary data
summary = dict()
length = len(bank_df["Date"])
summary["Total Months"] = length
summary["Total"] = bank_df["Profit/Losses"].sum()
summary["Average Change"] = bank_df["Monthly Change"].loc[1:length-1].mean()
summary["Max Increase"] = [month_max, delta_max]
summary["Max Decrease"] = [month_min, delta_min]


# write report to the terminal
generate_report(sys.stdout,summary)

# write report to an output file
output_file = os.path.join(my_dir, "analysis/summary.txt")
with open(output_file, "w") as f:
    generate_report(f,summary)
    f.close()
