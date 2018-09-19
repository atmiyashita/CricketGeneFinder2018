#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:58:32 2018

@author: atmiyashita
"""

import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  
    
from GeneFinder import GeneFinder
GeneFinder(ProteinName="lysozyme", db = "SRR6761207_TrinityAssembled_180515.fasta")
