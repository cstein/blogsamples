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
  """This function matches a SMARTS pattern to a molecule
  """
  obpat = openbabel.OBSmartsPattern()
  obpat.Init(pattern)
  obpat.Match(mol)
  return [m for m in obpat.GetUMapList()]

def OBMolMinimize(mol):
  """Minimize a molecule
  """
  ff = openbabel.OBForceField.FindForceField("MMFF94")
  ff.Setup(mol)
  ff.ConjugateGradients(100, 1.0e-5)
  return mol

def OBStructureFromSmiles(smilesstring, filename=None):
  mol = openbabel.OBMol()
  obConversion = openbabel.OBConversion()
  obConversion.SetInAndOutFormats("smi", "pdb")
  obConversion.ReadString(mol, smilesstring)
  mol.AddHydrogens() #False, True, 7.4)
  builder = openbabel.OBBuilder()
  builder.Build(mol)
  mol = OBMolMinimize(mol)
  if filename is None: return mol
  # save structures in subfolder molecules
  obConversion.WriteFile(mol, "molecules/%s.pdb" % filename)
