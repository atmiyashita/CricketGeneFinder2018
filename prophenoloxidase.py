#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: atmiyashita
"""

# %% Setup 
import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/2017-18/Shelley/Primer Design/Python')  
os.getcwd()

#####################################
                                    #
SearchTerm = "prophenoloxidase"     # <!---  ENTER THE SEARCH TERM (This is the only thing you need to do)
                                    # 
#####################################

# Load Packages
from Bio import Entrez # import Entrez
import subprocess
import xml.etree.ElementTree as ET

# ENVIRONMENT Settings
                            
 
ResPath = '/Users/atmiyashita/Google\ Drive/2017-18/Shelley/Primer\ Design/Python/'                                    
DatabaseName = 'Gryllus_rubens_bimac_firmus_TranscriptomeX3'
ArthropodSeqFileName = SearchTerm + "-arth.txt"
BlastResXmlFileName = "Blastres-" + SearchTerm + "-TrX3.xml"
Entrez.email ="atmiyashita@dal.ca"   # always tell NCBI who you are
BlastnPath = '/usr/local/ncbi/blast/bin/blastn'


#  <<<<<<<<   NCBI Search and downloading sequence file in a fasta format >>>>>>>

# open search and search taeget genes in arthropod (limit sequence length less than 10kbp)   
search_handle = Entrez.esearch(db="nucleotide",
                               term= '"' + SearchTerm
                               + '"[PROTEINFULLNAME] AND "arthropods"[porgn] AND 0:30000[Sequence Length]',
                               usehistory="y", idtype="acc",
                               RetMax=3000) 
search_record = Entrez.read(search_handle)              #store search record
search_handle.close()       #close search
print("The number of genes found in NCBI database is " + search_record["Count"] + ".")
print("The sequence data is now being downloaded and stored in '" + ArthropodSeqFileName + "'.")
IDs = search_record["IdList"]       #NCBI IDs (nucleotide) to fetch later
out_handle = open(ArthropodSeqFileName, "w+")       # open file where you save the result to      
for seq_id in IDs:
    fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, idtype="Gene",
                                 rettype="fasta",retmode="text") #fetch sequcences of each IDs above
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)    
out_handle.close()

#  <<<<<<< BLAST, saving the result in a xml file  >>>>>>>>>>>>>>>>>> 
print("Executing local BLAST (blastn) with " + DatabaseName +".fasta ...")
cmd_list = [BlastnPath,'-db', DatabaseName,
            '-query',ArthropodSeqFileName,
            '-out', BlastResXmlFileName,
            '-outfmt','5', '-evalue', '0.5']
subprocess.run(cmd_list)
print("The BLAST output xml file is saved as " + BlastResXmlFileName + ".")

#  <<<<<  Filter BLAST result, saving to a text file >>>>>>>>
tree = ET.parse("Blastres-" + SearchTerm + "-trX3.xml")
root = tree.getroot()
query = root[8]     #assing new object 'query' to root[8] for convenience
SeqSelectedFilename = "Blastres-" + SearchTerm + "-selected.txt"
res = open(SeqSelectedFilename, "w+")
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
print("The selected sequence names in " + DatabaseName + " have been saved in " + SeqSelectedFilename)