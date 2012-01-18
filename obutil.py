#
import openbabel

# quench tedious output of non-conforming pdb-format
openbabel.obErrorLog.SetOutputLevel(-1)

def OBMolFromFilename(filename):
  obmol = openbabel.OBMol()
  obconv = openbabel.OBConversion()
  obconv.SetInFormat("pdb")
  obconv.ReadFile(obmol, filename)
  return obmol

def OBMolToFilename(obmol, filename):
  obconv = openbabel.OBConversion()
  obconv.SetOutFormat("pdb")
  obconv.WriteFile(obmol, filename)

def OBAtomFromIndex(mol, index):
  return mol.GetAtom(index)

def OBSmartMatches(mol, pattern):
  obpat = openbabel.OBSmartsPattern()
  obpat.Init(pattern)
  obpat.Match(mol)
  return [m for m in obpat.GetUMapList()]

