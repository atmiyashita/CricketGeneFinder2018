#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:47:51 2018

@author: atmiyashita
"""

import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  

from GeneFinder import GeneFinder
GeneFinder(ProteinName="prophenoloxidase", db = "SRR6761207_TrinityAssembled_180515.fasta")
