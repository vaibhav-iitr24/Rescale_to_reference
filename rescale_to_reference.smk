import sys
import pandas as pd


run_df = pd.read_csv("data/run_metadata.tsv", sep="\t", header=0)
sample_df = pd.read_csv("data/sample.tsv", sep="\t", header=0)

run_df.index = run_df["run"]
sample_df.index = sample_df["sample"]

def get_all_runs_for_a_sample(wildcards):
    all_runs = sample_df.loc[wildcards.sample, "runs"].split(",")
    run_path_list = []
    for r in all_runs:
        p = run_df.loc[r, "file_path"]
        run_path_list.append(p)
    return run_path_list

rule frequency:
    input:
        all_runs=lambda wildcards: get_all_runs_for_a_sample(wildcards)
    output:
        frequency_file="generated_{sample}/frequency_{sample}.tsv",
        merged_file="generated_{sample}/merged_file_{sample}.tsv"
    shell:
        "sh scripts/freq.sh \"{input.all_runs}\" \"{output.merged_file}\" \"{output.frequency_file}\""

rule extraction:
    input:
        frequency_file="generated_{sample}/frequency_{sample}.tsv",
        merged_file="generated_{sample}/merged_file_{sample}.tsv"
    output:
        extracted="generated_{sample}/extracted_{sample}.tsv"
    shell:
        "python scripts/extraction.py \"{input.frequency_file}\" \"{input.merged_file}\" \"{output.extracted}\""

rule plot_graph:
    input:
        extracted="generated_{sample}/extracted_{sample}.tsv"
    output:
        plot="generated_{sample}/comparison_graph_{sample}.png"
    shell:
       "python scripts/graph.py \"{input.extracted}\" \"{output.plot}\""
