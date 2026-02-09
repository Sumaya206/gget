import gget
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import os

def disordered_plot():
        fig, ax = plt.subplots(figsize=(17,5))
    fontsize = 14

    # Plot IUPred2 scores returned by API
    scores = r.json()["iupred2"]
    ax.plot(np.arange(len(scores)+1)[1:], scores, lw=2)

    # Set x and y axis labels
    ax.set_xlabel("Residue", fontsize=fontsize)
    ax.set_ylabel("IUPred2 score", fontsize=fontsize)

    ax.axhline(0.5, color="black", lw=1, ls="--", zorder=-1)
    ax.text(0, 0.52, " ↑ Disordered", fontsize=fontsize-2)
    ax.text(0, 0.45, " ↓ Ordered", fontsize=fontsize-2)

    ax.set_ylim(0,1)
    ax.margins(x=0)
    ax.tick_params(axis="both", labelsize=fontsize)
    ax.grid(True, which="both", color="lightgray", ls="--", lw=1)
    ax.set_axisbelow(True)

    fig.show()

def find_disorder_regions(sequence, iupred_type="long"):

    with open("temp.seq", "w") as f:
        f.write(sequence)
    
    result = subprocess.run(
        ["python", "iupred3.py", "temp.seq", iupred_type],
        capture_output=True,
        text=True
    )

    os.remove("temp.seq")
    return result.stout

    # Get amino acid positions of all disordered residues (thresholded as IUPred score > 0.5)
    disordered = np.arange(len(scores)+1)[1:][np.array(scores) > 0.5]

    # Get amino acid positions of all ordered residues (thresholded as IUPred score < 0.5)
    ordered = np.arange(len(scores)+1)[1:][np.array(scores) < 0.5]

def is_subset(arr1, arr2):
  """
  Function to check if an array (arr2) is a subset of anoter array (arr1).

  Rerturns True is arr2 is a subset of arr1.
  """
  m = len(arr1)
  n = len(arr2)
  s = set()
  for i in range(m):
      s.add(arr1[i])

  p = len(s)
  for i in range(n):
      s.add(arr2[i])

  if (len(s) == p):
    return True
  else:
    return False

# Categorize each motif based on the IUPred scores of its residues

iupred = []
for index, row in regex.iterrows():
  # Get the start and end amino acid positions of the motif
  start = row['motif_start_in_query']
  end = row['motif_end_in_query']

  # Check if all positions covered by the motif are within ordered or disordered IUPred scores thresholds
  if is_subset(ordered, list(range(start, end+1))):
    iupred.append("ordered")

  elif is_subset(disordered, list(range(start, end+1))):
    iupred.append("disordered")

  else:
    iupred.append("inbetween")

# Add IUPred categorization to the regex dataframe
regex["IUPred"] = iupred

# Only keey motifs that fall into ordered protein regions
# regex[regex["IUPred"] == "disordered"]