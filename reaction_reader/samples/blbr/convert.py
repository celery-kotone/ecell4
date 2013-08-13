from ecell4.reaction_reader.decorator2 import species_attributes, reaction_rules
from ecell4.reaction_reader.species import generate_reactions, convert2bng_seed_species, convert2bng_reaction_rules, convert2bng_moleculetypes
from blbr import attributegen, rulegen


convert2bng_seed_species( attributegen() )
convert2bng_reaction_rules( rulegen() )
convert2bng_moleculetypes( rulegen() )
