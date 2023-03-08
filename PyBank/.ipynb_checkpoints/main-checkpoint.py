{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "58f07fe1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "------------------ \n",
      "Total Months: 86\n",
      "Total: $22,564,198.00\n",
      "Average Change: -$8,311.11\n",
      "Greatest Increase in Profits: Aug-16 ($1,862,002.00)\n",
      "Greatest Decrease in Profits: Feb-14 (-$1,825,558.00)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import sys\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import locale\n",
    "locale.setlocale(locale.LC_ALL, '')\n",
    "\n",
    "def generate_report(output_dev):\n",
    "    output_dev.write(\"Financial Analysis\\n------------------ \\n\")\n",
    "    output_dev.write(\"Total Months: \" + str(summary[\"Total Months\"]) + \"\\n\")\n",
    "    output_dev.write(\"Total: \" + locale.currency(summary[\"Total\"], grouping=True) + \"\\n\")\n",
    "    output_dev.write(\"Average Change: \" + locale.currency(summary[\"Average Change\"], grouping=True) + \"\\n\")\n",
    "    output_dev.write(\"Greatest Increase in Profits: \" + summary[\"Max Increase\"][0] + \" (\" + locale.currency(summary[\"Max Increase\"][1], grouping=True) + \")\\n\")\n",
    "    output_dev.write(\"Greatest Decrease in Profits: \" + summary[\"Max Decrease\"][0] + \" (\" + locale.currency(summary[\"Max Decrease\"][1], grouping=True) + \")\\n\")\n",
    "\n",
    "# get the data and load it into a data frame\n",
    "my_dir = os.getcwd()\n",
    "data_file = os.path.join(my_dir, \"Resources/budget_data.csv\")\n",
    "\n",
    "bank_df = pd.read_csv(data_file, encoding=\"utf-8\")\n",
    "\n",
    "\n",
    "# create a monthly change column in the bank dataframe\n",
    "# while we're looping, find max and min change information\n",
    "delta = np.array([float(\"nan\")])\n",
    "delta_max = 0\n",
    "delta_min = 0\n",
    "for i in range(1,len(bank_df)):\n",
    "    delta = np.append(delta, (bank_df[\"Profit/Losses\"][i] - bank_df[\"Profit/Losses\"][i-1]))\n",
    "    if delta[i] > delta_max:\n",
    "        delta_max = delta[i]\n",
    "        month_max = bank_df[\"Date\"][i]\n",
    "    if delta[i] < delta_min:\n",
    "        delta_min = delta[i]\n",
    "        month_min = bank_df[\"Date\"][i]\n",
    "bank_df[\"Monthly Change\"] = delta.tolist()\n",
    "\n",
    "\n",
    "# generate summary data\n",
    "summary = dict()\n",
    "length = len(bank_df[\"Date\"])\n",
    "summary[\"Total Months\"] = length\n",
    "summary[\"Total\"] = bank_df[\"Profit/Losses\"].sum()\n",
    "summary[\"Average Change\"] = bank_df[\"Monthly Change\"].loc[1:length-1].mean()\n",
    "summary[\"Max Increase\"] = [month_max, delta_max]\n",
    "summary[\"Max Decrease\"] = [month_min, delta_min]\n",
    "\n",
    "\n",
    "# write report to the terminal\n",
    "generate_report(sys.stdout)\n",
    "\n",
    "# write report to an output file\n",
    "output_file = os.path.join(my_dir, \"analysis/summary.txt\")\n",
    "with open(output_file, \"w\") as f:\n",
    "    generate_report(f)\n",
    "    f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee064fd8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
