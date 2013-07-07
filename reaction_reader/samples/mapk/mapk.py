from ecell4.reaction_reader.decorator import just_parse, reaction_rules


# @reaction_rules
@just_parse
def reactions(kon, koff, kcat):
    mapk(phos=YT) + kk(bs) > mapk(phos=YT^1).kk(bs^1) | kon
    mapk(phos=YT^1).kk(bs^1) > mapk(phos=YT) + kk(bs) | koff
    mapk(phos=YT^1).kk(bs^1) > mapk(phos=pYT) + kk(bs) | kcat

    mapk(phos=pYT) + pp(bs) == mapk(phos=pYT^1).pp(bs^1) | (kon, koff)
    mapk(phos=pYT^1).pp(bs^1) > mapk(phos=YT) + pp(bs) | kcat

    mapk(phos=pYT) + kk(bs) <> mapk(phos=pYT^1).kk(bs^1) | (kon, koff)
    mapk(phos=pYT^1).kk(bs^1) > mapk(phos=pYpT) + kk(bs) | kcat

    (mapk(phos=pYpT) + pp(bs)
        == mapk(phos=pYpT^1).pp(bs^1) | (kon, koff)
        > mapk(phos=pYT) + pp(bs) | kcat)

    (mapk(phos=YT) + kk(bs)
         == mapk(phos=YT^1).kk(bs^1) | (kon, koff)
         > mapk(phos=pYT) + kk(bs) | kcat
         == mapk(phos=pYT^1).kk(bs^1) | (kon, koff)
         > mapk(phos=pYpT) + kk(bs) | kcat)

    # (mapk(phos=pYpT) + pp(bs)
    #     == mapk(phos=pYpT^1).pp(bs^1) | (kon, koff)
    #     > mapk(phos=pYT) + pp(bs) | kcat
    #     == mapk(phos=pYT^1).pp(bs^1) | (kon, koff)
    #     > mapk(phos=YT) + pp(bs) | kcat)

def discribe_reaction(rr):
    fst = True
    literal = ""
    for s in rr.reactants():
        if fst != True:
            literal += " + "
        else:
            fst = False
        literal += s.name()
    literal += " => "
    fst = True
    for s in rr.products():
        if fst != True:
            literal += " + "
            fst = False
        else:
            fst = False
        literal += s.name()
    literal += "   | "
    literal += str( rr.k() )
    return literal

if __name__ == "__main__":
    rules = reactions(1, 2, 3)
    #import ipdb; ipdb.set_trace()
    for i, rr in enumerate(rules):
        #print i + 1, rr
        print  i + 1, discribe_reaction(rr)
