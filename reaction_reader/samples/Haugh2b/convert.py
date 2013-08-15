from ecell4.reaction_reader.decorator2 import species_attributes, reaction_rules
from ecell4.reaction_reader.species import generate_reactions, convert2bng_seed_species, convert2bng_reaction_rules, convert2bng_moleculetypes, export_bng
from Haugh2b import attributegen, rulegen

with open("export.bngl", "w") as fd:
    export_bng(fd, attributegen(0.5), 
            rulegen(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,
                8.0, 9.0, 10.0, 11.0))

