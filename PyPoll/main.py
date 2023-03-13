import os
import sys
import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, '')

# Generate an election results report to the output device passed as a parameter.
# It could be a file or the stdout (the terminal).
def generate_report(output_dev):
    output_dev.write("Election Results\n------------------------- \n")
    output_dev.write("Total Votes: " + str(votes_cast) + "\n")
    output_dev.write("------------------------- \n")
    for index, row in results_df.iterrows():
        output_dev.write(index + ": " + "{:.3%}".format(row['Percentage Votes']) + " (" + str(int(row['Total Votes'])) + ")\n")
    output_dev.write("------------------------- \n")
    output_dev.write("Winner: " + winner + "\n")
    output_dev.write("------------------------- \n")

# get the data and load it into a data frame
my_dir = os.getcwd()
data_file = os.path.join(my_dir, "Resources/election_data.csv")

election_df = pd.read_csv(data_file, encoding="utf-8")


# generate summary data
votes_cast = len(election_df)
results_df = pd.DataFrame()
results_df['Total Votes'] = election_df['Candidate'].value_counts()
results_df['Percentage Votes'] = results_df['Total Votes'] / votes_cast
winner = results_df['Total Votes'].idxmax()



# write report to the terminal
generate_report(sys.stdout)

# write report to an output file
output_file = os.path.join(my_dir, "analysis/results.txt")
with open(output_file, "w") as f:
    generate_report(f)
    f.close()
