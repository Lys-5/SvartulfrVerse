import json

lexicon_entries = [
    {
        "name": "DDM - Contractors",
        "keys": ["Contractor", "Contractors", "The Council"],
        "content": "In the DDM universe, Contractors are individuals bound to The Council through a reality-altering contract. They possess an ARC (Absolute Reality Control) level that determines their ability to bend reality. Upon becoming a Contractor, anyone who was consciously aware of their mortal existence ceases to exist. They see how they died on the Dead Dog Motel's sign.",
        "is_global": False,
        "type": "lore/concept"
    },
    {
        "name": "DDM - ACES",
        "keys": ["ACE", "ACES", "soulbond", "heat suppressants"],
        "content": "ACES are mortals who have willingly entered a soulbond with a Contractor. This grants them enhanced healing and longevity, but makes them biologically reliant on their Contractor. If separated for more than 24 hours, ACES enter a painful 'heat' that can only be alleviated by intimacy with their Contractor or specific heat suppressants (pills made from the Contractor's biological matter). If their Contractor dies, the ACE loses their mind.",
        "is_global": False,
        "type": "lore/concept"
    },
    {
        "name": "DDM - ARC Level",
        "keys": ["ARC", "ARC Level", "Absolute Reality Control"],
        "content": "Absolute Reality Control (ARC) measures a Contractor's power to bend reality. Higher ARC levels can override lower ones (e.g., memory alteration by a high-ARC Contractor overrides a low-ARC one). ARC is influenced by responsibility and mental drive, and rarely elevates naturally.",
        "is_global": False,
        "type": "lore/concept"
    },
    {
        "name": "DDM - SERAPHIM & The Broken Altar",
        "keys": ["Seraphim", "The Broken Altar Incident", "Raphael"],
        "content": "SERAPHIM are powerful entities, with Raphael formerly being Contractor #01. During 'The Broken Altar Incident' centuries ago, Raphael broke free of his Contract, losing his number tattoo and attempting to destroy the multiverse/Council to find a true purpose. His memories were erased from other Contractors, and Richard took his spot as #01.",
        "is_global": False,
        "type": "lore/concept"
    },
    {
        "name": "Dead Dog Motel / Voidspace",
        "keys": ["Dead Dog Motel", "DDM", "Voidspace"],
        "content": "The Dead Dog Motel is a multidimensional hub located in the Voidspace, serving as the headquarters for Contractors, ACES, and Mortals. Mortals sometimes wander in by accident and become trapped as employees. Time in the Voidspace is inconsistent relative to other dimensions.",
        "is_global": False,
        "type": "location"
    }
]

with open(r'd:\SvartulfrVerse\docs\DDM_Lexicon_Proposal.json', 'w', encoding='utf-8') as f:
    json.dump(lexicon_entries, f, indent=4)
print("DDM Lexicon Proposal generated.")
