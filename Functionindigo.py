# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:35:43 2018

@author: john3
"""
import indigo

g=indigo.Indigo()


m1=g.loadMolecule("CN(C)CCOC1=CC=C(C=C1)C(=C(CCCl)C2=CC=CC=C2)C3=CC=CC=C3")
m2=g.loadMolecule("CCN(CC)CCOC1=CC=C(C=C1)C(=C(C2=CC=CC=C2)Cl)C3=CC=CC=C3.C(C(=O)O)C(CC(=O)O)(C(=O)O)O")
m1.aromatize()
m2.aromatize()

print(m1.countAtoms())
print(m2.countAtoms())

fp1=m1.fingerprint('sim')
fp2=m2.fingerprint('sim')

print("  Tanimoto: %s" % (g.similarity(fp1, fp2, 
"tanimoto")))

#raloxifene smiles
#C1CCN(CC1)CCOC2=CC=C(C=C2)C(=O)C3=C(SC4=C3C=CC(=C4)O)C5=CC=C(C=C5)O

#toremifene smiles
#CN(C)CCOC1=CC=C(C=C1)C(=C(CCCl)C2=CC=CC=C2)C3=CC=CC=C3

#fispemifene smiles
#C1=CC=C(C=C1)C(=C(C2=CC=CC=C2)C3=CC=C(C=C3)OCCOCCO)CCCl

#enclomifene
#CCN(CC)CCOC1=CC=C(C=C1)C(=C(C2=CC=CC=C2)Cl)C3=CC=CC=C3.C(C(=O)O)C(CC(=O)O)(C(=O)O)O