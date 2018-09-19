#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:32:43 2018

@author: atmiyashita
"""

import os

os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  
    
from GeneFinder import GeneFinder
GeneFinder(ProteinName="cecropin", db = "SRR6761207_TrinityAssembled_180515.fasta")
GeneFinder(ProteinName="defensin", db = "SRR6761207_TrinityAssembled_180515.fasta")
GeneFinder(ProteinName="antimicrobial", db = "SRR6761207_TrinityAssembled_180515.fasta")
GeneFinder(ProteinName="lectin", db = "SRR6761207_TrinityAssembled_180515.fasta")

