
from ecell4.reaction_reader.decorator2 import species_attributes, reaction_rules
from ecell4.reaction_reader.species import generate_reactions, convert2bng_seed_species

@species_attributes
def attributegen():
    R0 = 14 
    L0 = 15
    # R(r,r) | R0
    A(r1,r2) | R0
    # L(l,l) | L0
    B(l1,l2) | L0

Kp1 = 1.0
Kp2 = 1.0

@reaction_rules
def rulegen():
    A(x=_1) > B(y=_1)   | Kp1
    A(x=_1) + B(y=_1) > A(x=_1^1).B(y=_1^1) | Kp2 
