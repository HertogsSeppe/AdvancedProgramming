import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem

from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole

smiles = [
    'N#CC(OC1OC(COC2OC(CO)C(O)C(O)C2O)C(O)C(O)C1O)c1ccccc1',
    'c1ccc2c(c1)ccc1c2ccc2c3ccccc3ccc21',
    'C=C(C)C1Cc2c(ccc3c2OC2COc4cc(OC)c(OC)cc4C2C3=O)O1',
    'ClC(Cl)=C(c1ccc(Cl)cc1)c1ccc(Cl)cc1'
]


mols = [Chem.MolFromSmiles(smi) for smi in smiles]

Draw.MolsToGridImage(mols, molsPerRow=2, subImgSize=(200, 200))