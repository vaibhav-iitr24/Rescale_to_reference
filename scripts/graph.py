import sys
import pandas as pd
import matplotlib.pyplot as plt

extracted= sys.argv[1]
plot= sys.argv[2]

df_extracted = pd.read_csv(extracted, sep='\t', header=None, names=['chrom', 'startpoint', 'endpoint', 'lena', 'lenb', 'match'],usecols=['chrom', 'startpoint', 'endpoint'])
df_reference= pd.read_csv('data/reference.hist', sep='\t', header=None, names=['dna_length', 'normalized_frequency'])


df_extracted['dna_length'] = df_extracted['endpoint'] - df_extracted['startpoint']
freq_merged = df_extracted['dna_length'].value_counts().sort_index()

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].bar(freq_merged.index, freq_merged.values, color='skyblue')
ax[0].set_title('DNA Length vs Frequency from extracted file')
ax[0].set_xlabel('DNA Length')
ax[0].set_ylabel('Frequency')


ax[1].bar(df_reference['dna_length'], df_reference['normalized_frequency'], color='salmon')
ax[1].set_title('DNA Length vs Normalized Frequency from reference.hist')
ax[1].set_xlabel('DNA Length')
ax[1].set_ylabel('Normalized Frequency')

plt.tight_layout()
plt.savefig(plot)
plt.show()
