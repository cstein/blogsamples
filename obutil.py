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

def OBAtomFromIndex(mol, index):
  return mol.GetAtom(index)

def OBSmartMatches(mol, pattern):
  obpat = openbabel.OBSmartsPattern()
  obpat.Init(pattern)
  obpat.Match(mol)
  return [m for m in obpat.GetUMapList()]
