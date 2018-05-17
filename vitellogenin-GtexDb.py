import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  

from GeneFinder import GeneFinder
GeneFinder(ProteinName="yolk protein", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder_tblastx
GeneFinder_tblastx(ProteinName="yolk protein", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder_tblastx
GeneFinder_tblastx(ProteinName="vitellogenin", db = "SRR6761207_TrinityAssembled_180515.fasta")
#  <<<<<  Filter BLAST result, saving to a text file >>>>>>>>   Set e-value threshold 1e-20
    os.chdir('/Users/atmiyashita/Google Drive/2017-18/Shelley/Primer Design/Python')  
    BlastResXmlFileName = "Blastres-vitellogenin_SRR6761207_TrinityAssembled_180515.fasta.xml"
    db ="SRR6761207_TrinityAssembled_180515"
    import xml.etree.ElementTree as ET
    tree = ET.parse(BlastResXmlFileName)
    root = tree.getroot()
    query = root[8]     #assing new object 'query' to root[8] for convenience
    SeqSelectedFilename = "Blastres-SELECTED_Eval-20_Vitellogenin" + db + "-selected.txt"
    res = open(SeqSelectedFilename, "w+")
    for itr in range(0, len(query)):
        if (len(query[itr][4]) > 0):        # if there is one or more hits, and
            query_hits = query[itr][4]
            if (int(query[itr][3].text) < 100000):   #if query length is less than 100000
                for Hits_i in range(0, len(query_hits)):
                    query_hits_i = query_hits[Hits_i]
                    query_hits_i_hsps_Hsp =query_hits_i[5][0]
                    Eval = query_hits_i_hsps_Hsp[3].text #e-value
                    queryname = query[itr][2].text
                    
                    if "vitellogenin" in queryname:
                        if "vitellogenin receptor" not in queryname:
                            if float(Eval) < 1e-20:
                                res.write("Hit_id (fasta name in db) = " + query_hits_i[1].text +'\n') # print name of gene (fasta name) in database they the query sequence was matched to
                                res.write("Hit_def (fasta name in db) = " + query_hits_i[2].text +'\n') # print name of gene (fasta name) in database they the query sequence was matched to 
                                res.write("itr with hit = " + str(itr) +'\n' ) # print query number
                                res.write("Query name = " + query[itr][2].text +'\n')   # print name of the query (gene name)
                                res.write("Query length = " + query[itr][3].text +'\n') # print query length
                                res.write("E-value = " + Eval +'\n') #print E-value
                                res.write("=============================" +'\n')
    res.close()
    
    "abc" not in "abc dfegfsa"


from GeneFinder import GeneFinder
GeneFinder(ProteinName="vitellogenin", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="vtg", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="yolk", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="Yp", db = "SRR6761207_TrinityAssembled_180515.fasta")
