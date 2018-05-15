import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  

from GeneFinder import GeneFinder
GeneFinder(ProteinName="vitellogenin", db = "SRR6761207_TrinityAssembled_180515.fasta")
