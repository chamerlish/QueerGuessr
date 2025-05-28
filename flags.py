# This file is meant to link the flags with the responses, by just using a dictionary in the format: {"response": "image-filename"}

flags = {
    "Ally": {
        "image": "ally.jpg",
        "hint": "Supports equality for all.",
        "keywords": ("Ally",),
    },

    "Lesbian": {
        "image": "lesbian.jpg",
        "hint": "Women loving women.",
        "keywords": ("Lesbian", "Les"),
    },

    "Butch Lesbian": {
        "image": "butch-lesbian.jpg",
        "hint": "A more masculine lesbian identity.",
        "keywords": ("Butch Lesbian", "Butch"),
    },

    "Labrys Lesbian": {
        "image": "labrys-lesbian.jpg",
        "hint": "Known for the labrys symbol.",
        "keywords": ("Labrys Lesbian", "Labrys"),
    },

    "Demiromantic": {
        "image": "demiromantic.jpg",
        "hint": "Romantic feelings develop after strong emotional bond.",
        "keywords": ("Demiromantic",),
    },

    "Demisexual": {
        "image": "demisexual.jpg",
        "hint": "Sexual attraction after emotional connection.",
        "keywords": ("Demisexual", "Demisex"),
    },

    "Bisexual": {
        "image": "bisexual.jpg",
        "hint": "Attracted to two or more genders.",
        "keywords": ("Bisexual", "Bi"),
    },

    "Pansexual": {
        "image": "pansexual.jpg",
        "hint": "Attracted regardless of gender.",
        "keywords": ("Pansexual", "Pan"),
    },

    "Omnisexual": {
        "image": "omnisexual.jpg",
        "hint": "Similar to pansexual but acknowledges gender.",
        "keywords": ("Omnisexual", "Omni"),
    },

    "Polysexual": {
        "image": "polysexual.jpg",
        "hint": "Attracted to multiple, but not all, genders.",
        "keywords": ("Polysexual",),
    },

    "Polyamorous": {
        "image": "polyamorous.jpg",
        "hint": "Multiple consensual romantic relationships.",
        "keywords": ("Polyamorous",),
    },

    "Femboy": {
        "image": "femboy.png",
        "hint": "A boy with feminine traits.",
        "keywords": ("Femboy",),
    },

    "Transgender": {
        "image": "transgender.jpg",
        "hint": "Gender identity differs from assigned sex.",
        "keywords": ("Transgender", "Trans"),
    },

    "Transandrogynous": {
        "image": "transandrogynous.png",
        "hint": "Blending transgender and androgynous identities.",
        "keywords": ("Transandrogynous",),
    },

    "Transmasculine": {
        "image": "transmasc.jpg",
        "hint": "More masculine gender identity assigned female at birth.",
        "keywords": ("Transmasculine", "Transmasc"),
    },

    "Transfeminine": {
        "image": "transfem.png",
        "hint": "More feminine gender identity assigned male at birth.",
        "keywords": ("Transfeminine", "Transfem"),
    },

    "Genderfluid": {
        "image": "genderfluid.jpg",
        "hint": "Gender identity shifts over time.",
        "keywords": ("Genderfluid", "Fluid"),
    },

    "Non-Binary": {
        "image": "non-binary.jpg",
        "hint": "Gender outside the binary man/woman.",
        "keywords": ("Non-Binary", "Non-Bi", "NB"),
    },

    "Intersex": {
        "image": "intersex.jpg",
        "hint": "Born with reproductive or sexual anatomy that doesn’t fit typical definitions.",
        "keywords": ("Intersex", "Inter"),
    },

    "Agender": {
        "image": "agender.jpg",
        "hint": "No gender identity.",
        "keywords": ("Agender",),
    },

    "Genderqueer": {
        "image": "genderqueer.jpg",
        "hint": "Gender outside or beyond the binary.",
        "keywords": ("Genderqueer",),
    },

    "Xenogender": {
        "image": "xenogender.png",
        "hint": "Gender identity beyond conventional categories.",
        "keywords": ("Xenogender", "Xeno"),
    },

    "Two Spirit": {
        "image": "two-spirit.jpg",
        "hint": "Indigenous North American gender identity.",
        "keywords": ("Two Spirit",),
    },

    "Asexual": {
        "image": "asexual.jpg",
        "hint": "Little or no sexual attraction to others.",
        "keywords": ("Asexual", "Ace"),
    },
}


import random
def get_random_flag():
    return random.choice(list(flags.items()))