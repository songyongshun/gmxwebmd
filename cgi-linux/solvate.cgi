#!/home/dcj/miniconda3/bin/python
# -*- coding: utf-8 -*-

import sys
import cgi
from autogmx import autorun,cd_solvate
sys.stdout.write("Content-Type: text/plain\n\n")

autorun(cd_solvate)
