#!/usr/bin/env python
"""
contact_number.py - calculate the contact number
"""
import pylab
import openbabel

filename = "1CRN.pdb"
pattern = "[$(CC(=O)[N,O])]"
obmol = openbabel.OBMol()
obconv = openbabel.OBConversion()
obpat = openbabel.OBSmartsPattern()
obconv.SetInFormat(filename[-3:])
obconv.ReadFile(obmol, filename)
obpat.Init(pattern)
obpat.Match(obmol)
alpha_carbons = [m[0] for m in obpat.GetUMapList()]

def ContactNumbersForCutoff(matches, rcut):
  contact_numbers = []
  for i in matches:
    contact_number = 0
    ai = obmol.GetAtom(i)
    for j in matches:
      if i == j: continue
      aj = obmol.GetAtom(j)
      if ai.GetDistance(aj) < rcut:
        contact_number +=1

    contact_numbers.append(contact_number)
  return contact_numbers

cn12 = ContactNumbersForCutoff(alpha_carbons,12.0)
pylab.title("Contact Number for Residues in Crambine")
pylab.ylabel("$\\alpha$-carbon count")
pylab.xlabel("residue number")
pylab.plot(cn12,label="$R_{cut}=12.0$", linewidth=2.0)
pylab.legend()
pylab.savefig("contact.png")
