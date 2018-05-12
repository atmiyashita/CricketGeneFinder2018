#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:59:41 2017

@author: atmiyashita
"""

# %%  <<<<<<<<   NCBI Search and downloading sequence file in a fasta format >>>>>>>
from Bio import Entrez # import Entrez
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
search_handle = Entrez.esearch(db="nucleotide", term='"antimicrobial peptide"[All field] AND "arthropods"[porgn] AND 0:30000[Sequence Length]',
                               usehistory="y", idtype="acc",RetMax=1000) # open search and search taeget genes in arthropod (limit sequence length less than 30kbp)   !<<----Check!
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print(search_record["Count"])
print(search_record["IdList"])
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
print(search_record.keys())
print(IDs)
out_handle = open("AMPs-arth.txt", "w")       # open file where you save the result to                                 !<<----Check!
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()





from Bio import Entrez # import Entrez
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
search_handle = Entrez.esearch(db="nucleotide", term='"moricin"[All field] AND "arthropods"[porgn] AND 0:30000[Sequence Length]',
                               usehistory="y", idtype="acc",RetMax=1000) # open search and search taeget genes in arthropod (limit sequence length less than 30kbp)   !<<----Check!
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print(search_record["Count"])
print(search_record["IdList"])
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
print(search_record.keys())
print(IDs)
out_handle = open("Moricin-arth.txt", "w")       # open file where you save the result to                                 !<<----Check!
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()





from Bio import Entrez # import Entrez
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
search_handle = Entrez.esearch(db="nucleotide", term='"cecropin"[All field] AND "arthropods"[porgn] AND 0:30000[Sequence Length]',
                               usehistory="y", idtype="acc",RetMax=1000) # open search and search taeget genes in arthropod (limit sequence length less than 30kbp)   !<<----Check!
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print(search_record["Count"])
print(search_record["IdList"])
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
print(search_record.keys())
print(IDs)
out_handle = open("Cecropin-arth.txt", "w")       # open file where you save the result to                                 !<<----Check!
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()






from Bio import Entrez # import Entrez
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
search_handle = Entrez.esearch(db="nucleotide", term='"defensin"[All field] AND "arthropods"[porgn] AND 0:30000[Sequence Length]',
                               usehistory="y", idtype="acc",RetMax=1000) # open search and search taeget genes in arthropod (limit sequence length less than 30kbp)   !<<----Check!
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print(search_record["Count"])
print(search_record["IdList"])
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
print(search_record.keys())
print(IDs)
out_handle = open("Defensin-arth.txt", "w")       # open file where you save the result to                                 !<<----Check!
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()





from Bio import Entrez # import Entrez
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
search_handle = Entrez.esearch(db="nucleotide", term='"attacin"[All field] AND "arthropods"[porgn] AND 0:30000[Sequence Length]',
                               usehistory="y", idtype="acc",RetMax=1000) # open search and search taeget genes in arthropod (limit sequence length less than 30kbp)   !<<----Check!
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print(search_record["Count"])
print(search_record["IdList"])
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
print(search_record.keys())
print(IDs)
out_handle = open("Attacin-arth.txt", "w")       # open file where you save the result to                                 !<<----Check!
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()


# %%  <<<<<<< BLAST, saving the result in a xml file  >>>>>>>>>>>>>>>>>> %% Currently not working -> command directily from terminal! 
import subprocess
subprocess.call('blastn -db tr2.fasta -query GPx-arth.txt -out Blastres-GPx-tr2.xml -outfmt 5 -evalue 1e-5')     

# %% <<<<<  Filter BLAST result, saving to a text file >>>>>>>>
import xml.etree.ElementTree as ET
tree = ET.parse("Blastres-AMPs-trX3.xml")                                        #!<<----Check!
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
res = open("Blastres-AMPs-selected.txt", "w")                                #!<<----Check!
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





import xml.etree.ElementTree as ET
tree = ET.parse("Blastres-Moricin-trX3.xml")                                        #!<<----Check!
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
res = open("Blastres-Moricin-selected.txt", "w")                                #!<<----Check!
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






import xml.etree.ElementTree as ET
tree = ET.parse("Blastres-Cecropin-trX3.xml")                                        #!<<----Check!
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
res = open("Blastres-Cecropin-selected.txt", "w")                                #!<<----Check!
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







import xml.etree.ElementTree as ET
tree = ET.parse("Blastres-Defensin-trX3.xml")                                        #!<<----Check!
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
res = open("Blastres-Defensin-selected.txt", "w")                                #!<<----Check!
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







import xml.etree.ElementTree as ET
tree = ET.parse("Blastres-Attacin-trX3.xml")                                        #!<<----Check!
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
res = open("Blastres-Attacin-selected.txt", "w")                                #!<<----Check!
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