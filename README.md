# Rescale_to_reference
1] In project directory(main directory) another directory "data" created to store input data. I have 2 files of one sample analysis i.e. shuf.a.bed.gz and shuf.b.bed.gz downloaded from website - https://figshare.com/s/2d3d4d60a82de9cc3cc6 using 'curl -JLO' and stored it into data directory. These files unziped by using 'gunzip' command[Not able to upload here because of file size]. Also there is reference file in data directory, we have rescale our data to that reference file.

2] Again two files created sample.tsv and run_metadat.tsv in data directory. sample.tsv contain information of sample and their runs and in run_metadata.tsv contain runs and their respective path.

3] Scripts directory created in main directory, contain scripts for to obtain frequency, to extract lines and plot graph. 

4] Snakemake(rescale_to_reference.smk) file created in main directory, required scripts and rules are incorporated. Snakemake environment activated, run command  " snakemake --snakefile rescale_to_reference.smk generated_demo/comparison_graph_demo.png -j1". Here demo is sample name you can change it as per requirement.
