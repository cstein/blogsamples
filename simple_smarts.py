#!/usr/bin/env python
"""
simple_smarts.py - simple example on how to use SMARTS patterns
                   via the Open Babel API
"""
import openbabel

filename = '1UAO.pdb'
pattern = "[$(CN)][$(C=O)]"

# OpenBabel utilities
obmol = openbabel.OBMol()
obconv = openbabel.OBConversion()
obpat = openbabel.OBSmartsPattern()

# load the molecule
obconv.SetInFormat(filename[-3:])
obconv.ReadFile(obmol, filename)

# initialize pattern matching
obpat.Init(pattern)

# apply pattern matching to the molecule
obpat.Match(obmol)

# avoid getting lots of <openbabel.vectorvInt; proxy ... > etc.
matches = [m for m in obpat.GetUMapList()]
print matches
