# GeneFinder

This is a repository for python codes for a program that searches for a gene fragment in fragmentary database (such as transcriptome contig sequences) based on BLAST homology search.

The scheme of this program is

1. Download all the sequence data from NCBI database associated with a gene name (protein name) of interest
2. Run a BLAST search locally using your own database, such as a transcriptome dataset (in fasta format).
3. Extract relevant informations from the output file (xml format)
