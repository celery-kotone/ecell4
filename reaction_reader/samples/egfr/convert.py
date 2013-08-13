from ecell4.reaction_reader.decorator2 import species_attributes, reaction_rules
from ecell4.reaction_reader.species import generate_reactions, convert2bng_seed_species, convert2bng_reaction_rules, convert2bng_moleculetypes, export_bng
from egfr import attributegen, rulegen

with open("export.bngl", "w") as fd:
    export_bng(fd, attributegen(), rulegen())

