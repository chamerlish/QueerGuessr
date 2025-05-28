# This file is meant to link the flags with the responses, by just using a dictionary in the format: {"response": "image-filename"}

flags = {
    ("Ally"): "ally.jpg",

    ("Lesbian", "Les"): "lesbian.jpg",
    ("Butch Lesbian", "Butch"): "butch-lesbian.jpg",
    ("Labrys Lesbian", "Labrys"): "labrys-lesbian.jpg",
    # "Gay": "gay.jpg",
    
    ("Demiromantic"): "demiromantic.jpg",
    ("Demisexual", "Demisex"): "demisexual.jpg",

    ("Bisexual", "Bi"): "bisexual.jpg",
    ("Pansexual", "Pan"): "pansexual.jpg",
    
    ("Omnisexual", "Omni"): "omnisexual.jpg",
    ("Polysexual"): "polysexual.jpg",
    ("Polyamorous"): "polyamorous.jpg",
    ("Polyamorous"): "poluamorous.png",

    ("Femboy"): "femboy.png",
    ("Transgender", "Trans"): "transgender.jpg",
    ("Transandrogynous"): "transandrogynous.png",
    ("Transmasculine", "Transmasc"): "transmasc.jpg",
    ("Transfeminine", "Transfem"): "transfem.png",


    ("Genderfluid", "Fluid"): "genderfluid.jpg",

    ("Non-Binary", "Non-Bi", "NB"): "non-binary.jpg",
    ("Intersex", "Inter"): "intersex.jpg",
    ("Agender"): "agender.jpg",
    
    ("Genderqueer"): "genderqueer.jpg",
    ("Xenogender", "Xeno"): "xenogender.png",

    ("Two Spirit"): "two-spirit.jpg",

    ("Asexual", "Ace"): "asexual.jpg",
}

import random
def get_random_flag():
    return random.choice(list(flags.items()))