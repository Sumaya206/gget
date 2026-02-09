import gget
import pandas as pd
from pathlib import Path
from Bio import SeqIO

input_dir = Path("my_modules/ELM_motif_query/input_folder")
output_dir = Path("my_modules/ELM_motif_query/output_folder")
output_dir.mkdir(parents=True, exist_ok=True)

gget.setup("elm")

def search_elm_motifs(input_dir):

    pd.set_option('display.max_columns', None)

    for input_file in input_dir.glob("*.fasta"):
        for record in SeqIO.parse(input_file, "fasta"):
            print(f"Processing {record.id}...")

            ortholog_df, regex_df = gget.elm(str(record.seq), uniprot=False, expand=True)

            if ortholog_df is not None and not ortholog_df.empty:
                ortholog_name = output_dir / f"{record.id}_elm_ortholog_results.csv"

                # ortholog df contains info about DIAMOND alignment
                ortholog_df.to_csv(ortholog_name, index=False)

            if regex_df is not None and not regex_df.empty:
                regex_name = output_dir / f"{record.id}_elm_motif_results.csv"

                # regex df contains ELM motifs matching in sequence
                regex_df.to_csv(regex_name, index=False)

if __name__ == "__main__":

    search_elm_motifs(input_dir)