#!/usr/bin/env python3
# fonction qui génére un monstre avec des attributs différents

def generation_du_monstre():
    import random
    PV = random.randrange(5,20)
    Force = random.randrange(3,8)
    Armure = random.randrange(0,5)
    monstre = [PV, Force, Armure]
    return(monstre)

