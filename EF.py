#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:52:24 2017

@author: atmiyashita
"""
# %%  <<<<<<<<   NCBI Search and downloading sequence file in a fasta format >>>>>>>
from Bio import Entrez # import Entrez
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
search_handle = Entrez.esearch(db="nucleotide", term='"elongation factor"[PROTEINFULLNAME] AND "arthropods"[porgn] AND 0:10000[Sequence Length]',
                               usehistory="y", idtype="acc",RetMax=1000) # open search and search taeget genes in arthropod (limit sequence length less than 10kbp)   !<<----Check!
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print(search_record["Count"])
print(search_record["IdList"])
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
print(search_record.keys())
print(IDs)
out_handle = open("EF-arth.txt", "w")       # open file where you save the result to                                 !<<----Check!
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()


# %%  <<<<<<< BLAST, saving the result in a xml file  >>>>>>>>>>>>>>>>>> %% Currently not working -> command directily from terminal! 
import subprocess
subprocess.call('blastn -db tr2.fasta -query EF-arth.txt -out Blastres-EF-tr2.xml -outfmt 5 -evalue 1e-5')     

# %%
import xml.etree.ElementTree as ET
tree = ET.parse("Blastres-EF-tr2.xml")                                        #!<<----Check!
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
res = open("Blastres-EF-selected.txt", "w")
for itr in range(0, len(query)):
    if (len(query[itr][4]) > 0):        # if there is one or more hits, and
        query_hits = query[itr][4]
        if (int(query[itr][3].text) < 10000):   #if query length is less than 10000
            for Hits_i in range(0, len(query_hits)):
                query_hits_i = query_hits[Hits_i]
                query_hits_i_hsps_Hsp =query_hits_i[5][0]
                Eval = query_hits_i_hsps_Hsp[3].text #e-value
                if float(Eval) < 1e-05:
                    res.write("Hit_def (fasta name in db) = " + query_hits_i[2].text +'\n') # print name of gene (fasta name) in database they the query sequence was matched to 
                    res.write("itr with hit = " + str(itr) +'\n' ) # print query number
                    res.write("Query name = " + query[itr][2].text +'\n')   # print name of the query (gene name)
                    res.write("Query length = " + query[itr][3].text +'\n') # print query length
                    res.write("E-value = " + Eval +'\n') #print E-value
                    res.write("=============================" +'\n')
res.close()