import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  

from GeneFinder import GeneFinder
GeneFinder(ProteinName="yolk protein", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder_tblastx
GeneFinder_tblastx(ProteinName="yolk protein", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="vitellogenin", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="vtg", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="yolk", db = "SRR6761207_TrinityAssembled_180515.fasta")

from GeneFinder import GeneFinder
GeneFinder(ProteinName="Yp", db = "SRR6761207_TrinityAssembled_180515.fasta")
