from __future__ import print_function
from rdkit import Chem

def handleUploadFile(f):    
    with open('static/media/molecule.txt','w+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        # rdkit   
        stringWithMolData=destination.read()
        mol = Chem.MolFromMolBlock(stringWithMolData)
        smiles = Chem.MolToSmiles(mol)
    
    return smiles
    # else:
        # return 'File type Error!'
    