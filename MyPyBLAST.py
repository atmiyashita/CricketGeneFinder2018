#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:59:49 2018

@author: atmiyashita
"""



query="TEST.fasta"
def Blastx_LOCAL (query, eval_threshold=0.001):
    import subprocess
    import xml.etree.ElementTree as ET
    SearchTerm = query
    DatabaseName = "/Volumes/hdd2014/db/nr.all/combined_nr"
    print("Executing local BLAST (blastx), using " + DatabaseName +" as database...")
    BlastResXmlFileName = "Blastx_" + SearchTerm + ".xml"
    cmd_list = ['/usr/local/ncbi/blast/bin/blastx','-db', DatabaseName,
                '-query',SearchTerm,
                '-out', BlastResXmlFileName,
                '-outfmt','5', '-evalue', str(eval_threshold)]
    subprocess.run(cmd_list)
    print("The BLAST output xml file is saved as " + BlastResXmlFileName + ".")
    tree = ET.parse(BlastResXmlFileName)
    root = tree.getroot()
    query = root[8]     #assing new object 'query' to root[8] for convenience
    SeqSelectedFilename = "Blastx-SELECTED_" + SearchTerm  + ".txt"
    res = open(SeqSelectedFilename, "w+")
    for itr in range(0, len(query)):
        if (len(query[itr][4]) > 0):        # if there is one or more hits, and
            query_hits = query[itr][4]
            if (int(query[itr][3].text) < 100000):   #if query length is less than 100000
                for Hits_i in range(0, len(query_hits)):
                    query_hits_i = query_hits[Hits_i]
                    query_hits_i_hsps_Hsp =query_hits_i[5][0]
                    Eval = query_hits_i_hsps_Hsp[3].text #e-value
                    if float(Eval) < 1e-03:
                        res.write("Hit_id (fasta name in db) = " + query_hits_i[1].text +'\n') # print name of gene (fasta name) in database they the query sequence was matched to
                        res.write("Hit_def (fasta name in db) = " + query_hits_i[2].text +'\n') # print name of gene (fasta name) in database they the query sequence was matched to 
                        res.write("itr with hit = " + str(itr) +'\n' ) # print query number
                        res.write("Query name = " + query[itr][2].text +'\n')   # print name of the query (gene name)
                        res.write("Query length = " + query[itr][3].text +'\n') # print query length
                        res.write("E-value = " + Eval +'\n') #print E-value
                        res.write("=============================" +'\n')
                        res.close()
    print("The selected sequence names in " + DatabaseName + " have been saved in " + SeqSelectedFilename)
    print("End of the process. Congrats!")
