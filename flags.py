# This file is meant to link the flags with the responses, by just using a dictionary in the format: {"response": "image-filename"}

flags = {
    ("Ally",): {
        "image": "ally.jpg",
        "hint": "Supports equality for all.",
        "description": "The Ally flag represents support for the LGBTQ+ community."
    },

    ("Lesbian", "Les"): {
        "image": "lesbian.jpg",
        "hint": "Women loving women.",
        "description": "The Lesbian flag is for women who love women."
    },

    ("Butch Lesbian", "Butch"): {
        "image": "butch-lesbian.jpg",
        "hint": "A more masculine lesbian identity.",
        "description": "The Butch Lesbian flag represents lesbians with masculine traits."
    },

    ("Labrys Lesbian", "Labrys"): {
        "image": "labrys-lesbian.jpg",
        "hint": "Known for the labrys symbol.",
        "description": "The Labrys Lesbian flag features the double-headed axe symbol."
    },

    # ("Gay"): "gay.jpg",  # You can add this as needed

    ("Demiromantic",): {
        "image": "demiromantic.jpg",
        "hint": "Romantic feelings develop after strong emotional bond.",
        "description": "The Demiromantic flag represents people who develop romantic feelings after close emotional connections."
    },

    ("Demisexual", "Demisex"): {
        "image": "demisexual.jpg",
        "hint": "Sexual attraction after emotional connection.",
        "description": "The Demisexual flag represents people who experience sexual attraction only after emotional bonding."
    },

    ("Bisexual", "Bi"): {
        "image": "bisexual.jpg",
        "hint": "Attracted to two or more genders.",
        "description": "The Bisexual flag represents attraction to both the same and different genders."
    },

    ("Pansexual", "Pan"): {
        "image": "pansexual.jpg",
        "hint": "Attracted regardless of gender.",
        "description": "The Pansexual flag represents attraction to all genders."
    },

    ("Omnisexual", "Omni"): {
        "image": "omnisexual.jpg",
        "hint": "Similar to pansexual but acknowledges gender.",
        "description": "The Omnisexual flag represents attraction to all genders but with recognition of gender."
    },

    ("Polysexual",): {
        "image": "polysexual.jpg",
        "hint": "Attracted to multiple, but not all, genders.",
        "description": "The Polysexual flag represents attraction to multiple genders, but not all."
    },

    ("Polyamorous",): {
        "image": "polyamorous.jpg",
        "hint": "Multiple consensual romantic relationships.",
        "description": "The Polyamorous flag represents people who have multiple romantic relationships with consent."
    },

    ("Femboy",): {
        "image": "femboy.png",
        "hint": "A boy with feminine traits.",
        "description": "The Femboy flag represents males who express femininity."
    },

    ("Transgender", "Trans"): {
        "image": "transgender.jpg",
        "hint": "Gender identity differs from assigned sex.",
        "description": "The Transgender flag represents people whose gender identity differs from the sex they were assigned at birth."
    },

    ("Transandrogynous",): {
        "image": "transandrogynous.png",
        "hint": "Blending transgender and androgynous identities.",
        "description": "The Transandrogynous flag represents a blend of transgender and androgynous identities."
    },

    ("Transmasculine", "Transmasc"): {
        "image": "transmasc.jpg",
        "hint": "More masculine gender identity assigned female at birth.",
        "description": "The Transmasculine flag represents people assigned female at birth but identifying more masculinely."
    },

    ("Transfeminine", "Transfem"): {
        "image": "transfem.png",
        "hint": "More feminine gender identity assigned male at birth.",
        "description": "The Transfeminine flag represents people assigned male at birth but identifying more femininely."
    },

    ("Genderfluid", "Fluid"): {
        "image": "genderfluid.jpg",
        "hint": "Gender identity shifts over time.",
        "description": "The Genderfluid flag represents people whose gender identity fluctuates."
    },

    ("Non-Binary", "Non-Bi", "NB"): {
        "image": "non-binary.jpg",
        "hint": "Gender outside the binary man/woman.",
        "description": "The Non-Binary flag represents people whose gender doesn't fit strictly as male or female."
    },

    ("Intersex", "Inter"): {
        "image": "intersex.jpg",
        "hint": "Born with reproductive or sexual anatomy that doesn’t fit typical definitions.",
        "description": "The Intersex flag represents people with intersex traits."
    },

    ("Agender",): {
        "image": "agender.jpg",
        "hint": "No gender identity.",
        "description": "The Agender flag represents people who identify as having no gender."
    },

    ("Genderqueer",): {
        "image": "genderqueer.jpg",
        "hint": "Gender outside or beyond the binary.",
        "description": "The Genderqueer flag represents people who reject traditional gender distinctions."
    },

    ("Xenogender", "Xeno"): {
        "image": "xenogender.png",
        "hint": "Gender identity beyond conventional categories.",
        "description": "The Xenogender flag represents genders that are difficult to describe in traditional terms."
    },

    ("Two Spirit",): {
        "image": "two-spirit.jpg",
        "hint": "Indigenous North American gender identity.",
        "description": "The Two Spirit flag represents a traditional Indigenous North American gender role."
    },

    ("Asexual", "Ace"): {
        "image": "asexual.jpg",
        "hint": "Little or no sexual attraction to others.",
        "description": "The Asexual flag represents people who experience little or no sexual attraction."
    },
}


import random
def get_random_flag():
    return random.choice(list(flags.items()))