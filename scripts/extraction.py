import sys
import pandas as pd


frequency_file = sys.argv[1]
merged_file = sys.argv[2]
output_file = sys.argv[3]

freq_df = pd.read_csv(frequency_file, sep='\t', header=None, names=['length', 'frequency'])

ref_df = pd.read_csv('data/reference.hist', sep='\t', header=None, names=['Length', 'normalized_frequency'])

High_nfr= ref_df['normalized_frequency'].max()

length_with_highest_nfr = ref_df.loc[ref_df['normalized_frequency'] == High_nfr, 'Length'].values[0]
#print(length_with_highest_nfr)

z = freq_df.loc[freq_df['length'] == length_with_highest_nfr, 'frequency'].values[0]
#print(z)


required_lines={}

for index, rows in ref_df.iterrows():
    length = rows['Length']
    nfr = rows['normalized_frequency']
    if length in freq_df['length'].values:
        frequency=freq_df.loc[freq_df['length'] ==length, 'frequency'].values[0]

        required_lines[length] = round((nfr / High_nfr) * z)

#print(required_lines)


extracted_lines=[]

with open(merged_file,'r') as all_merged_file:
    for line in all_merged_file:
        fields=line.split()
        start_position=int(fields[1])
        end_position=int(fields[2])
        line_length=end_position-start_position
        if line_length in required_lines:
            req_lines=int(required_lines[line_length])
            if req_lines>0:
                extracted_lines.append(line)
                required_lines[line_length]-=1

#print(required_lines)
with open(output_file, 'w') as output_file:
       output_file.writelines(extracted_lines)
