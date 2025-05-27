# This file is meant to link the flags with the responses, by just using a dictionary in the format: {"response": "image-filename"}

flags = {
    "Ally": "ally.jpg",

    "Lesbian": "lesbian.jpg",
    "Butch Lesbian": "butch-lesbian.jpg",
    "Labrys Lesbian": "labrys-lesbian.jpg",
    # "Gay": "gay.jpg",
    
    "Demiromantic": "demiromantic.jpg",
    "Demibisexual": "demibisexual.jpg",

    "Bisexual": "bisexual.jpg",
    "Pansexual": "pansexual.jpg",
    
    "Omnisexual": "omnisexual.jpg",
    "Polysexual": "polysexual.jpg",
    "Polyamorous": "polyamorous.jpg",
    
    "Demisexual": "demisexual.jpg",
    "Demiromantic": "demiromantic.jpg",

    "Genderfluid": "genderfluid.jpg",

    "Non-Binary": "non-binary.jpg",
    "Intersex": "intersex.jpg",
    "Agender": "agender.jpg",
    "Asexual": "asexual.jpg",

    "Two Spirit": "two-spirit.jpg",
}

import random
def get_random_flag():
    return random.choice(list(flags.items()))