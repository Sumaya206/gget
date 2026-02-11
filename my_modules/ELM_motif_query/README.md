## Overview

This pipeline is a bioinformatics tool for analyzing **alphavirus protein sequences** in a way that is **customizable, reproducible, and scalable**. It scans protein FASTA files for **Short Linear Motifs (SLiMs)** using the **ELM database**, allowing many sequences to be analyzed at once.

The pipeline is written in **Python** and primarily uses the **`gget`** package to efficiently query ELM data. Because it runs locally, it is **faster and more flexible** than the online ELM website and does not limit how many sequences can be submitted at a time.

## Running the Scripts

All scripts in this pipeline are run from the command line using Python.

The general format looks like this:

    python "relative/path/to/script.py" --flag_name value

You can find the relative path my right clicking on file 'tab' or file in browser on left side, then selecting 'Copy Relative Path'.

Currently, there are no relevant flags that you should add to your command.

## Using ELM motif query Scripts
### Input
Input FASTA formated files should be moved into the input folder, which can be found at:

    my_modules/ELM_motif_query/input_folder

You can enter individual or multi-record FASTA files as the input for this module, it will process one or more files that end with ".fasta" in the input folder.

### Function of gget elm
My script is adapted to iteratively loop over the 'gget.elm' for every FASTA sequence and create the 'gget.elm' output files named for each sequence.

Ortholog file: ELM finds similar related proteins in other 'species', this will likely bring up other alphaviruses.
Regex file: ELM uses 'regular expressions' to identify short linear motifs (SLiMs) encoded within a provided sequence

### Outputs

The output files from a successful run should be in the output folder, which can be either found at 

    my_modules/ELM_motif_query/output_folder

or in a folder that will be created with the name 'output_folder' when you run the script if it doesn't yet exist.

## Saving your work to GitHub

The following commands entered in the terminal will help you upload your current work to your GitHub account.

To add the files you want to save to the GitHub staging area, use the command:

    git add .

Then to 'commit' these changes and add a message descriping the changes or updates you have made:

    git commit -m "Description of your changes"

Lastly,  to upload these committed changes to GitHub 'cloud' online, use the command:

    git push origin <branch-name>

In this case, your branch name will show up in '()' in your terminal command line after the current pathway. 

This should print out a summary in the terminal, such as:

    Enumerating objects: 7, done.
    Counting objects: 100% (7/7), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (4/4), 724 bytes | 724.00 KiB/s, done.
    Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
    To https://github.com/tiiafreeman/gget_bioinformatics
    7dd2f78..38810ef  gget_elm -> gget_elmZ