#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:15:34 2018

@author: atmiyashita
"""

import os
os.getcwd()
os.chdir('/Users/atmiyashita/Google Drive/GitHub/GeneFinder/')  

from GeneFinder import GeneFinder_tblastx
GeneFinder_tblastx(ProteinName="vitellogenin", db = "Gryllus_rubens_bimac_firmus_TranscriptomeX3")
