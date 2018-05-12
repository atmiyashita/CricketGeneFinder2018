# GeneFinder

This is a repository for python codes for a program that searches for a gene fragment in fragmentary database (such as transcriptome contig sequences) based on BLAST homology search.

The scheme of this program is

1. Download all the sequence data from NCBI database associated with a gene name (protein name) of interest
2. Run a BLAST search locally using your own database, such as a transcriptome dataset (in fasta format).
3. Extract relevant informations from the output file (xml format)

# The Main Function 

The main function is in 'GeneFinder.py', where a function 'GeneFinder' is defined. You can always call this function by executing the following in your python console (remember to set the working directory appropreately).

from GeneFinder import GeneFinder

## Files to store in this repository 

Due to the size limit in repositories in GitHub, I will not store large files (e.g. sequence database files) in this repository. They are saved locally or in Goole Drive.

Currently, 

 1. 'xxx.py' files 
 
is stored in this repository. Each '.py' files refer to Google Drive address in each code.
