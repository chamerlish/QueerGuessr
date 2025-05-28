# This file is meant to link the flags with the responses, by just using a dictionary in the format: {"response": "image-filename"}

flags = {
    "Ally": {
        "image": "ally.jpg",
        "hints": (
            "It's a form of support.",
            "Not part of the community itself.",
            "Supports equality for all.",
        ),
        "keywords": ("Ally",),
    },

    "Lesbian": {
        "image": "lesbian.jpg",
        "hints": (
            "It's a sexuality.",
            "Women loving women.",
            "One of the most well-known orientations.",
        ),
        "keywords": ("Lesbian", "Les"),
    },

    "Butch Lesbian": {
        "image": "butch-lesbian.jpg",
        "hints": (
            "A more specific lesbian identity.",
            "Often presents more masculine.",
            "Masculine-presenting lesbian.",
        ),
        "keywords": ("Butch Lesbian", "Butch"),
    },

    "Labrys Lesbian": {
        "image": "labrys-lesbian.jpg",
        "hints": (
            "Another type of lesbian identity.",
            "Associated with a double-headed axe.",
            "Known for the labrys symbol.",
        ),
        "keywords": ("Labrys Lesbian", "Labrys"),
    },

    "Demiromantic": {
        "image": "demiromantic.jpg",
        "hints": (
            "It's a romantic orientation.",
            "Needs emotional bond before attraction.",
            "Romantic feelings develop after emotional connection.",
        ),
        "keywords": ("Demiromantic",),
    },

    "Demisexual": {
        "image": "demisexual.jpg",
        "hints": (
            "It's a sexual orientation.",
            "Needs emotional bond before attraction.",
            "Sexual attraction after emotional connection.",
        ),
        "keywords": ("Demisexual", "Demisex"),
    },

    "Bisexual": {
        "image": "bisexual.jpg",
        "hints": (
            "It's a common orientation.",
            "Attracted to more than one gender.",
            "Attracted to two or more genders.",
        ),
        "keywords": ("Bisexual", "Bi"),
    },

    "Pansexual": {
        "image": "pansexual.jpg",
        "hints": (
            "Gender doesn't factor into attraction.",
            "Inclusive of all gender identities.",
            "Attracted regardless of gender.",
        ),
        "keywords": ("Pansexual", "Pan"),
    },

    "Omnisexual": {
        "image": "omnisexual.jpg",
        "hints": (
            "Similar to pansexual.",
            "Gender plays a role but doesn’t limit.",
            "Acknowledges gender but is still open.",
        ),
        "keywords": ("Omnisexual", "Omni"),
    },

    "Polysexual": {
        "image": "polysexual.jpg",
        "hints": (
            "Not attracted to everyone.",
            "Multiple but not all genders.",
            "Attracted to many, not all.",
        ),
        "keywords": ("Polysexual",),
    },

    "Polyamorous": {
        "image": "polyamorous.jpg",
        "hints": (
            "About relationships, not orientation.",
            "More than one romantic relationship.",
            "Multiple consensual romantic relationships.",
        ),
        "keywords": ("Polyamorous",),
    },

    "Femboy": {
        "image": "femboy.png",
        "hints": (
            "Gender expression focused.",
            "Masculine body, feminine traits.",
            "A boy with feminine traits.",
        ),
        "keywords": ("Femboy",),
    },

    "Transgender": {
        "image": "transgender.jpg",
        "hints": (
            "Gender identity related.",
            "Different from assigned sex at birth.",
            "Gender identity differs from assigned sex.",
        ),
        "keywords": ("Transgender", "Trans"),
    },

    "Transandrogynous": {
        "image": "transandrogynous.png",
        "hints": (
            "Mixes gender expressions.",
            "Androgynous and transgender.",
            "Blending transgender and androgynous identities.",
        ),
        "keywords": ("Transandrogynous",),
    },

    "Transmasculine": {
        "image": "transmasc.jpg",
        "hints": (
            "Masculine presenting.",
            "AFAB and identifies as masculine.",
            "More masculine gender identity assigned female at birth.",
        ),
        "keywords": ("Transmasculine", "Transmasc"),
    },

    "Transfeminine": {
        "image": "transfem.png",
        "hints": (
            "Feminine presenting.",
            "AMAB and identifies as feminine.",
            "More feminine gender identity assigned male at birth.",
        ),
        "keywords": ("Transfeminine", "Transfem"),
    },

    "Genderfluid": {
        "image": "genderfluid.jpg",
        "hints": (
            "Shifts over time.",
            "Not fixed in one gender.",
            "Gender identity shifts over time.",
        ),
        "keywords": ("Genderfluid", "Fluid"),
    },

    "Non-Binary": {
        "image": "non-binary.jpg",
        "hints": (
            "Not a man or woman.",
            "Exists outside the gender binary.",
            "Gender outside the binary man/woman.",
        ),
        "keywords": ("Non-Binary", "Non-Bi", "NB"),
    },

    "Intersex": {
        "image": "intersex.jpg",
        "hints": (
            "Biological variation.",
            "Not strictly male or female anatomy.",
            "Born with reproductive or sexual anatomy that doesn’t fit typical definitions.",
        ),
        "keywords": ("Intersex", "Inter"),
    },

    "Agender": {
        "image": "agender.jpg",
        "hints": (
            "No gender identity.",
            "Genderless or neutral.",
            "Identifies with no gender.",
        ),
        "keywords": ("Agender",),
    },

    "Genderqueer": {
        "image": "genderqueer.jpg",
        "hints": (
            "Queer gender identity.",
            "Outside the binary.",
            "Gender outside or beyond the binary.",
        ),
        "keywords": ("Genderqueer",),
    },

    "Xenogender": {
        "image": "xenogender.png",
        "hints": (
            "Unconventional gender concept.",
            "May use non-human concepts.",
            "Gender identity beyond conventional categories.",
        ),
        "keywords": ("Xenogender", "Xeno"),
    },

    "Two Spirit": {
        "image": "two-spirit.jpg",
        "hints": (
            "Indigenous identity.",
            "Cultural and spiritual role.",
            "Indigenous North American gender identity.",
        ),
        "keywords": ("Two Spirit",),
    },

    "Asexual": {
        "image": "asexual.jpg",
        "hints": (
            "Little or no sexual attraction.",
            "Not interested in sex.",
            "Little or no sexual attraction to others.",
        ),
        "keywords": ("Asexual", "Ace"),
    },
}


import random
def get_random_flag():
    return random.choice(list(flags.items()))
