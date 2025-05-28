# This file is meant to link the flags with the responses, by just using a dictionary in the format: {"response": "image-filename"}

flags = {
    "Ally": {
        "image": "ally.jpg",
        "hints": (
            "It's a form of support.",
            "Not part of the community itself.",
            "Supports equality for all...",
        ),
        "keywords": ("Ally",),
    },

    "Lesbian": {
        "image": "lesbian.jpg",
        "hints": (
            "It's a sexuality.",
            "Women loving women.",
            "One of the most well-known orientations...",
        ),
        "keywords": ("Lesbian", "Les"),
    },

    "Butch Lesbian": {
        "image": "butch-lesbian.jpg",
        "hints": (
            "It's a sexual orientation."
            "A more specific lesbian identity.",
            "Often presents more masculine...",
        ),
        "keywords": ("Butch Lesbian", "Butch"),
    },

    "Labrys Lesbian": {
        "image": "labrys-lesbian.jpg",
        "hints": (
            "It's a sexual orientation.",
            "Another type of lesbian identity.",
            "Very linked to feminist roots...",
        ),
        "keywords": ("Labrys Lesbian", "Labrys"),
    },

    "Demiromantic": {
        "image": "demiromantic.jpg",
        "hints": (
            "It's a romantic orientation.",
            "",
            "Romantic feelings develop after emotional connection...",
        ),
        "keywords": ("Demiromantic",),
    },

    "Demisexual": {
        "image": "demisexual.jpg",
        "hints": (
            "It's a sexual orientation.",
            "",
            "Sexual attraction after emotional connection...",
        ),
        "keywords": ("Demisexual", "Demisex"),
    },

    "Bisexual": {
        "image": "bisexual.jpg",
        "hints": (
            "It's a sexual orientation.",
            "*__GENERALLLY__* within \"gender\" boundaries.",
            "*See both sides like Chanel...*",
        ),
        "keywords": ("Bisexual", "Bi"),
    },

    "Pansexual": {
        "image": "pansexual.jpg",
        "hints": (
            "It's a sexual orientation.",
            "Inclusive of all gender identities.",
            "Attraction regardless of gender...",
        ),
        "keywords": ("Pansexual", "Pan"),
    },

    "Omnisexual": {
        "image": "omnisexual.jpg",
        "hints": (
            "It's a sexual orientation.",
            "Inclusive of all gender identities.",
            "Gender plays a role but doesn’t limit...",
        ),
        "keywords": ("Omnisexual", "Omni"),
    },

    "Polysexual": {
        "image": "polysexual.jpg",
        "hints": (
            "It's a sexual orientation.",
            "Inclusive of all gender identities.",
            "Attraction to two or more genders...",
        ),
        "keywords": ("Polysexual",),
    },

    "Polyamorous": {
        "image": "polyamorous.jpg",
        "hints": (
            "It's a romantic orientation.",
            "More of a relationship style.",
            "Multiple consensual romantic relationships...",
        ),
        "keywords": ("Polyamorous", "Polygamous", "Polygamy"),
    },

    "Femboy": {
        "image": "femboy.png",
        "hints": (
            "Gender expression focused.",
            "Considered within \"gender\" boundaries."
            "Masculine body, feminine traits...",
        ),
        "keywords": ("Femboy",),
    },

    "Transgender": {
        "image": "transgender.jpg",
        "hints": (
            "Gender expression focused.",
            "*__GENERALLLY__* within \"gender\" boundaries.",
            "Gender identity differing from assigned sex...",
        ),
        "keywords": ("Transgender", "Trans"),
    },

    "Transandrogynous": {
        "image": "transandrogynous.png",
        "hints": (
            "Gender expression focused.",
            "Beyond tipical gender boundaries.",
            "Blending transgender and androgynous identities...",
        ),
        "keywords": ("Transandrogynous",),
    },

    "Transmasculine": {
        "image": "transmasc.jpg",
        "hints": (
            "Gender expression focused.",
            "Can be beyond gender boundaries.",
            "A more masculine gender identity...",
        ),
        "keywords": ("Transmasculine", "Transmasc"),
    },

    "Transfeminine": {
        "image": "transfem.png",
        "hints": (
            "Gender expression focused.",
            "Can be beyond gender boundaries.",
            "A more feminine gender identity...",
        ),
        "keywords": ("Transfeminine", "Transfem"),
    },

    "Genderfluid": {
        "image": "genderfluid.jpg",
        "hints": (
            "Gender expression focused.",
            "Tipically considered beyond gender boundaries.",
            "Gender identity may shift over time...",
        ),
        "keywords": ("Genderfluid", "Fluid"),
    },

    "Non-Binary": {
        "image": "non-binary.jpg",
        "hints": (
            "Gender expression focused.",
            "Beyond gender boundaries.",
            "Umbrella term...",
        ),
        "keywords": ("Non-Binary", "Non-Bi", "NB"),
    },

    "Intersex": {
        "image": "intersex.jpg",
        "hints": (
            "Gender expression focused."
            "Biological variation.",
            "Born with reproductive or sexual anatomy that doesn’t fit typical definitions...",
        ),
        "keywords": ("Intersex", "Inter"),
    },

    "Agender": {
        "image": "agender.jpg",
        "hints": (
            "Gender expression focused.",
            "Beyond gender boundaries.",
            "A lack of gender identity...",
        ),
        "keywords": ("Agender",),
    },

    "Genderqueer": {
        "image": "genderqueer.jpg",
        "hints": (
            "Gender expression focused.",
            "Beyond gender boundaries...",
            "QUEER!",
        ),
        "keywords": ("Genderqueer",),
    },

    "Xenogender": {
        "image": "xenogender.png",
        "hints": (
            "Gender expression focused.",
            "Gender identity beyond conventional categories.",
            "May use non-human concepts...",
        ),
        "keywords": ("Xenogender", "Xeno"),
    },

    "Two Spirit": {
        "image": "regions/two-spirit.jpg",
        "hints": (
            "Sexual and Gender related oriontation.",
            "Cultural and spiritual role.",
            "Indigenous North American gender identity...",
        ),
        "keywords": ("Two Spirit",),
    },

    "Asexual": {
        "image": "asexual.jpg",
        "hints": (
            "it's a Sexual orientation.", 
            "",
            "Little or no sexual attraction to others....",
        ),
        "keywords": ("Asexual", "Ace"),
    },
}


import random
def get_random_flag():
    return random.choice(list(flags.items()))
