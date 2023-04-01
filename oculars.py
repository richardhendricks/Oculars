'''
This python script helps with using Stellarium's oculars.ini file.
It can take a single file and convert it to a CSV file.
It can take a single or multiple CSV files an convert them to
a combined INI file.
This allows easy editing using a spreadsheet, and combining things
like a personal set of equipment with a remote observatory such as 
iTelescope.net
'''

'''
python3 oculars.py <output file> <input file 1> (input file 2,etc)\n\n
'''

help_msg = '''
Script will determine based on output file extension (.ini or .csv) which
direction you wish to go.
\n
When outputting a CSV file, only one INI file input is allowed.
\n
When outputting an INI file, multiple input CSV files are allowed.
'''

'''
Data format
INI data format matches the stellarium oculars.ini input format.

CSV data format
First line is the group
Sucessive line is the item-specific data in that group (normally grouped
by number in the INI, the CSV makes them one horizontal line).
Blank line in between groups.
'''

import argparse
import configparser
import csv
import os

def create_ini():
    return

def create_csv(output, inputs):
    with open(output, "w") as outputfile:
        inputparser=configparser.ConfigParser()
        for input in inputs:
            inputparser.read(input)
        output_dict={}
        # Go over general
        for section in inputparser.sections():
            output_dict[section]={}
            for option in inputparser.options(section):
                output_dict[section][option]=inputparser.get(section,option)
        # Go over each subtype based on how many appear in general (not needed to create CSV)
        # output new dictionary
        with open(output, 'w') as outfile:
            for section in output_dict.keys():
                outfile.write('\n['+section+']\n')
                for option in output_dict[section]:
                    outfile.write(option+','+output_dict[section][option]+'\n')

    return

parser = argparse.ArgumentParser(description=help_msg)
parser.add_argument('output', type=str, help="Output file name. Extension determines operation.")
parser.add_argument('inputs', type=str, nargs="+", help="Input file(s)")
args = parser.parse_args()

output_ext = os.path.splitext(args.output)[1]

if(output_ext == ".ini"):
    print("Outputting INI file")
elif(output_ext == ".csv"):
    if len(args.inputs) > 1:
        print("Only provide 1 INI file!")
        exit(-2)
    print("Outputting CSV file")
    create_csv(args.output, args.inputs)
else:
    print("Unknown extension type!")
    exit(-1)

