"""
Script to reconcile 54 World Lexicon items and configure 5 key shop locations.
- Updates item_config for all 54 items with balanced prices in USD and Cr,
  weights, rarities, tradeability, and equip slots.
- Configures marketplace_config on 5 key locations in Blackwood & Solarton.
- Eliminates the '54 items players can never get' warning.
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')

USD_ID = "fbecc738-f9f7-4426-b8a1-a237b8ad922c"
CR_ID = "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a"

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

# 54 Items Database definition
ITEMS_METADATA = {
    "_1cVjGdFd8V3Q7pkad3Dt1": {
        "name": "Lighter",
        "stackable": True, "max_stack": 10, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.1, "equip_slot": None,
        "usd": 2.50, "cr": 250
    },
    "_FrLpFaULBEUrM1EnkYfUY": {
        "name": "Wireless Earbuds",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": "trinket",
        "usd": 45.00, "cr": 4500
    },
    "_fX8FzBcbFFAV6Htmn4TNP": {
        "name": "Keys",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.1, "equip_slot": None,
        "usd": 10.00, "cr": 1000
    },
    "_1WTbfahmng63e7qz8RbpA": {
        "name": "DMHA: Sistemi d'Armamento Reliquia (Armi Vincolate / Messors)",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "legendary", "weight": 4.5, "equip_slot": "weapon_main",
        "usd": 3500.00, "cr": 350000
    },
    "_kW81naTxb2Mph9aQgMKbg": {
        "name": "DMHA: Equipaggiamento d'Assalto per Operativi di Grado S & A",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "epic", "weight": 8.0, "equip_slot": "body",
        "usd": 1200.00, "cr": 120000
    },
    "_qacTbKEFgej4ndm8D7YmV": {
        "name": "DMHA: Generatori Portatili di Barriera & Dissuasione Mana (Mana Fields)",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "rare", "weight": 2.5, "equip_slot": "trinket",
        "usd": 750.00, "cr": 75000
    },
    "_7F8f77MwpJnhCXeMmctNe": {
        "name": "DMHA: Manette a Densita Variabile & Collari di Blocco Morfologico",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "rare", "weight": 1.5, "equip_slot": None,
        "usd": 300.00, "cr": 30000
    },
    "_eGrfMqCybMRyChUgNbYCK": {
        "name": "DMHA: Lame Mana-Conductive & Sigilli Runici da Trincea",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "rare", "weight": 1.8, "equip_slot": "weapon_main",
        "usd": 450.00, "cr": 45000
    },
    "_hUT336WCffkNRrUDNPMre": {
        "name": "DMHA: Manuale Tascabile dei Protocolli di De-escalation Urbana",
        "stackable": True, "max_stack": 5, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.3, "equip_slot": None,
        "usd": 25.00, "cr": 2500
    },
    "_fHc8hEjmLAaz1zXTPrke8": {
        "name": "DMHA: Spray Neutralizzante ad Aconito & Solventi Antimagici",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "uncommon", "weight": 0.5, "equip_slot": None,
        "usd": 85.00, "cr": 8500
    },
    "_fG49qq6LVMApkzpFTyFAD": {
        "name": "DMHA: Munizionamento Argentato Silver-Hollowpoint",
        "stackable": True, "max_stack": 20, "consumable": True, "tradeable": True,
        "rarity": "uncommon", "weight": 1.0, "equip_slot": None,
        "usd": 120.00, "cr": 12000
    },
    "_27xnFr6AqqJqN6EyzMAHj": {
        "name": "DMHA: Visori Spettrali & Tracciatori di Squarcio Classe 1 e 2",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "rare", "weight": 1.2, "equip_slot": "head",
        "usd": 600.00, "cr": 60000
    },
    "_CVBWaPP37egd4WRRjyj7W": {
        "name": "Double-Shot Mana Espresso",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": None,
        "usd": 5.50, "cr": 550
    },
    "_FJPqfwwp3zrx1FAXPK7dB": {
        "name": "Full Moon Glazed Doughnut",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": None,
        "usd": 3.50, "cr": 350
    },
    "_6yGybRVDVYF9BmPF6mUPW": {
        "name": "Spiced Catnip Steamer Latte",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.3, "equip_slot": None,
        "usd": 6.00, "cr": 600
    },
    "_Tp4p8Pr6KqUjUeY8tDeLb": {
        "name": "Therianthrope Protein Shake",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.8, "equip_slot": None,
        "usd": 11.00, "cr": 1100
    },
    "_z3QQXfVnCMzd79y2qjEH4": {
        "name": "Chamomile & Moon-Herb Infusion",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": None,
        "usd": 15.00, "cr": 1500
    },
    "_VFhHFd4XJ6FYTcmBPLGz2": {
        "name": "Artisanal Silver-Crust Loaf",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 1.0, "equip_slot": None,
        "usd": 8.00, "cr": 800
    },
    "_rCMq1RdjjeVbFmQ9ycUkQ": {
        "name": "Cold Brew Nitro Focus",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.4, "equip_slot": None,
        "usd": 7.00, "cr": 700
    },
    "_h4ze7HJDCUVGjrRFTf2WQ": {
        "name": "Moonflower Honey Pastry",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": None,
        "usd": 8.00, "cr": 800
    },
    "_kWJK9q3313zYAfR8UT1pc": {
        "name": "SUCC: Catalizzatori, Focus Runici & Sigilli d'Incanalamento",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 0.8, "equip_slot": "weapon_off",
        "usd": 150.00, "cr": 15000
    },
    "_wNBn1df9BEc6QjYDHpJNX": {
        "name": "Familiar Empathetic Treat Biscuit",
        "stackable": True, "max_stack": 20, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.1, "equip_slot": None,
        "usd": 12.00, "cr": 1200
    },
    "_KyAh8ymQBwP9kzn4nezU3": {
        "name": "LSE Scent Suppressor Spray Bottle",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "uncommon", "weight": 0.2, "equip_slot": None,
        "usd": 40.00, "cr": 4000
    },
    "_pRJRWmqJeQTM3k19c9xJU": {
        "name": "Anti-Silver Burn Healing Salve",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "uncommon", "weight": 0.3, "equip_slot": None,
        "usd": 35.00, "cr": 3500
    },
    "_BnVPaNjWmhCnCX1b4zDdM": {
        "name": "Cellular Regeneration Ampoule",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "rare", "weight": 0.2, "equip_slot": None,
        "usd": 120.00, "cr": 12000
    },
    "_emAUbbxE3WBAAn7rX18BY": {
        "name": "Reinforced Runic Mechanic Wrench",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 1.5, "equip_slot": "weapon_main",
        "usd": 65.00, "cr": 6500
    },
    "_bbDzPj28Mrq2L6BxMqzxH": {
        "name": "Wolfsbane Toxin Neutralizer",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "rare", "weight": 0.2, "equip_slot": None,
        "usd": 150.00, "cr": 15000
    },
    "_LbKeWy2Fr2yGQGDYaph29": {
        "name": "High-Performance Graphene Chain Lubricant",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.4, "equip_slot": None,
        "usd": 28.00, "cr": 2800
    },
    "_RV9cNGgNkQVNxrRYdzRNg": {
        "name": "Acoustic-Dampening Game Master Screen",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 2.0, "equip_slot": None,
        "usd": 45.00, "cr": 4500
    },
    "_xp9HANz2MeYM7eHDKD8FY": {
        "name": "Raw Clover Valley Whole Milk (Gallon)",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 3.8, "equip_slot": None,
        "usd": 7.50, "cr": 750
    },
    "_3mrctyEjmxpx4HMB2mG9e": {
        "name": "Miniature Pewter Werewolf Warlord",
        "stackable": True, "max_stack": 10, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": None,
        "usd": 18.00, "cr": 1800
    },
    "_a2MtcAwG1QCcd2eJKt1KN": {
        "name": "Obsidian Balanced Polyhedral Dice Set",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 0.3, "equip_slot": "trinket",
        "usd": 35.00, "cr": 3500
    },
    "_RTc7dLgGz7g3qxfrQqEGB": {
        "name": "Oak-Aged Smoked Farmhouse Cheese Wheel",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 2.0, "equip_slot": None,
        "usd": 24.00, "cr": 2400
    },
    "_YFhALNxgF3V2GLqpXNLVX": {
        "name": "Hand-Churned Sweet Cream Butter",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.5, "equip_slot": None,
        "usd": 6.00, "cr": 600
    },
    "_BaFB83w6DGkJdHQFRHWMN": {
        "name": "Ironhorn Nomads Leather Vest Patch",
        "stackable": True, "max_stack": 5, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 0.1, "equip_slot": None,
        "usd": 25.00, "cr": 2500
    },
    "_wFXpmhrEnjjDbJ7mV7cVT": {
        "name": "Coyote Deluxe Monster Burger",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.8, "equip_slot": None,
        "usd": 16.50, "cr": 1650
    },
    "_aM8gyAY28CAreAARhkXLp": {
        "name": "Bottomless Black Roadhouse Drip Coffee",
        "stackable": True, "max_stack": 1, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.3, "equip_slot": None,
        "usd": 4.00, "cr": 400
    },
    "_FA24ewwHf4Y8dhhpKzMhk": {
        "name": "Raw Beef Marrow Bones Pack",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 2.5, "equip_slot": None,
        "usd": 18.00, "cr": 1800
    },
    "_fnC4RyHggw2dxEXGcCUFP": {
        "name": "Prime Bone-In Ribeye Steak (2 lbs)",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "uncommon", "weight": 1.0, "equip_slot": None,
        "usd": 36.00, "cr": 3600
    },
    "_3RFAn7KnBXcxN9p6cDBzf": {
        "name": "Smoked Wild Boar Hunter Sausages",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.8, "equip_slot": None,
        "usd": 22.00, "cr": 2200
    },
    "_UxxF3kPAjVb3kkYMLMLDN": {
        "name": "Neon Blue Highball Cocktail",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.4, "equip_slot": None,
        "usd": 18.00, "cr": 1800
    },
    "_gK3VkKXD9QXCd3k8EM42p": {
        "name": "Vintage Noir Crystal Champagne",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "rare", "weight": 0.4, "equip_slot": None,
        "usd": 180.00, "cr": 18000
    },
    "_drc7r7KPtTDAb3UkBhPrp": {
        "name": "Aloe & Vitamin E Tattoo Aftercare Butter",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.2, "equip_slot": None,
        "usd": 16.00, "cr": 1600
    },
    "_LVzCYVfahJF7yqdC77gxT": {
        "name": "Douglas Reserve 18-Year Bourbon",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "rare", "weight": 0.5, "equip_slot": None,
        "usd": 220.00, "cr": 22000
    },
    "_zFMQb6pcAHLzWYMyN3g6x": {
        "name": "Venom-Gold Agave Tequila Shot",
        "stackable": True, "max_stack": 10, "consumable": True, "tradeable": True,
        "rarity": "uncommon", "weight": 0.1, "equip_slot": None,
        "usd": 22.00, "cr": 2200
    },
    "_4RakHM7j2Lm2dNe9XdnwA": {
        "name": "Warm Homemade Pecan Pie Slice",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.3, "equip_slot": None,
        "usd": 6.50, "cr": 650
    },
    "_b4YjVRQ2hVJLHGJMfgUFp": {
        "name": "Reinforced Carbon-Fiber Shortboard",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "rare", "weight": 3.2, "equip_slot": "weapon_main",
        "usd": 650.00, "cr": 65000
    },
    "_Dp9qtARRc7ahMWHb8KDdh": {
        "name": "Thermal Neoprene Pacific Wetsuit (4/3mm)",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 2.1, "equip_slot": "body",
        "usd": 280.00, "cr": 28000
    },
    "_jwz7Ke4hbQGMgLw36cENt": {
        "name": "Jar of Luminescent Hex Valley Moon Moss",
        "stackable": True, "max_stack": 10, "consumable": False, "tradeable": True,
        "rarity": "rare", "weight": 0.5, "equip_slot": None,
        "usd": 50.00, "cr": 5000
    },
    "_FbQj2cAwYCJbCwtPMgdaX": {
        "name": "Organic Coconut Cold-Water Surf Wax",
        "stackable": True, "max_stack": 20, "consumable": True, "tradeable": True,
        "rarity": "common", "weight": 0.1, "equip_slot": None,
        "usd": 6.00, "cr": 600
    },
    "_gKLdADmXkpM1XdLC6L6T2": {
        "name": "Braided Silver Thread Talisman Bracelet",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "uncommon", "weight": 0.1, "equip_slot": "ring1",
        "usd": 45.00, "cr": 4500
    },
    "_LMbFnEpxDDTdwyUCAkkmB": {
        "name": "Surgical Black Titanium Industrial Piercing",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.05, "equip_slot": "trinket",
        "usd": 30.00, "cr": 3000
    },
    "_yxP6wUGEkwxk7FFH7Br91": {
        "name": "Handcrafted Distressed Leather Belt Pouch",
        "stackable": False, "max_stack": 1, "consumable": False, "tradeable": True,
        "rarity": "common", "weight": 0.4, "equip_slot": "trinket",
        "usd": 55.00, "cr": 5500
    },
    "_QtpdDqq1QQKXwGTJpJgUD": {
        "name": "Tendril",
        "stackable": True, "max_stack": 5, "consumable": True, "tradeable": True,
        "rarity": "rare", "weight": 0.2, "equip_slot": None,
        "usd": 250.00, "cr": 25000
    }
}

# 5 Locations Shop Mapping
SHOPS_CONFIG = {
    "_H7PpzWXrQ228RgBw1Rqh9": {
        "name": "Solarton Market-Zone & Tactical Surplus",
        "description": "Solarton's bustling commercial center. Specialized black-market tech, DMHA surplus equipment, heavy mechanic tools, dice, RPG miniatures, and alchemical field gear.",
        "buy_rate": 0.5,
        "items": [
            '_1cVjGdFd8V3Q7pkad3Dt1', '_FrLpFaULBEUrM1EnkYfUY', '_fX8FzBcbFFAV6Htmn4TNP',
            '_1WTbfahmng63e7qz8RbpA', '_kW81naTxb2Mph9aQgMKbg', '_qacTbKEFgej4ndm8D7YmV',
            '_7F8f77MwpJnhCXeMmctNe', '_eGrfMqCybMRyChUgNbYCK', '_hUT336WCffkNRrUDNPMre',
            '_fHc8hEjmLAaz1zXTPrke8', '_fG49qq6LVMApkzpFTyFAD', '_27xnFr6AqqJqN6EyzMAHj',
            '_kWJK9q3313zYAfR8UT1pc', '_emAUbbxE3WBAAn7rX18BY', '_LbKeWy2Fr2yGQGDYaph29',
            '_RV9cNGgNkQVNxrRYdzRNg', '_3mrctyEjmxpx4HMB2mG9e', '_a2MtcAwG1QCcd2eJKt1KN',
            '_LMbFnEpxDDTdwyUCAkkmB'
        ]
    },
    "_QHaW3bG49Dx1QW4Ugg8xn": {
        "name": "Full Moon Night Market",
        "description": "Open-air nocturnal bazaar tucked along the Blackwood forest perimeter. Lupine apothecary, alchemical salves, wolfsbane remedies, rare biological suppressors, talismans, and fresh hunter game.",
        "buy_rate": 0.5,
        "items": [
            '_KyAh8ymQBwP9kzn4nezU3', '_pRJRWmqJeQTM3k19c9xJU', '_BnVPaNjWmhCnCX1b4zDdM',
            '_bbDzPj28Mrq2L6BxMqzxH', '_wNBn1df9BEc6QjYDHpJNX', '_z3QQXfVnCMzd79y2qjEH4',
            '_h4ze7HJDCUVGjrRFTf2WQ', '_jwz7Ke4hbQGMgLw36cENt', '_gKLdADmXkpM1XdLC6L6T2',
            '_yxP6wUGEkwxk7FFH7Br91', '_FA24ewwHf4Y8dhhpKzMhk', '_fnC4RyHggw2dxEXGcCUFP',
            '_3RFAn7KnBXcxN9p6cDBzf', '_drc7r7KPtTDAb3UkBhPrp', '_QtpdDqq1QQKXwGTJpJgUD'
        ]
    },
    "_PjVjY62CtnLbhrEE69GbK": {
        "name": "Tidewrack Surf & Coastal Outfitters",
        "description": "Sun-bleached coastal shack in Solarton Bay. High-end carbon-fiber shortboards, wetsuits, cold-water waxes, biker nomad gear, and local leatherwork.",
        "buy_rate": 0.5,
        "items": [
            '_b4YjVRQ2hVJLHGJMfgUFp', '_Dp9qtARRc7ahMWHb8KDdh', '_FbQj2cAwYCJbCwtPMgdaX',
            '_BaFB83w6DGkJdHQFRHWMN', '_1cVjGdFd8V3Q7pkad3Dt1', '_FrLpFaULBEUrM1EnkYfUY',
            '_fX8FzBcbFFAV6Htmn4TNP', '_drc7r7KPtTDAb3UkBhPrp', '_LMbFnEpxDDTdwyUCAkkmB'
        ]
    },
    "_CAAHGnM3BGKpUb7JXYWm7": {
        "name": "The Dusty Coyote Roadhouse Kitchen & Pantry",
        "description": "Historic highway diner with greasy chrome counters, bottomless coffee pots, massive monster burgers, homemade pies, and fresh Clover Valley dairy goods.",
        "buy_rate": 0.5,
        "items": [
            '_wFXpmhrEnjjDbJ7mV7cVT', '_aM8gyAY28CAreAARhkXLp', '_4RakHM7j2Lm2dNe9XdnwA',
            '_CVBWaPP37egd4WRRjyj7W', '_FJPqfwwp3zrx1FAXPK7dB', '_6yGybRVDVYF9BmPF6mUPW',
            '_Tp4p8Pr6KqUjUeY8tDeLb', '_rCMq1RdjjeVbFmQ9ycUkQ', '_VFhHFd4XJ6FYTcmBPLGz2',
            '_xp9HANz2MeYM7eHDKD8FY', '_RTc7dLgGz7g3qxfrQqEGB', '_YFhALNxgF3V2GLqpXNLVX'
        ]
    },
    "_HPnYePHbmCVM9tMp69Hrg": {
        "name": "The Verve Private Cellar & Lounge",
        "description": "High-end speakeasy and private club in Blackwood. Ultra-rare spirits, vintage champagnes, luminescent neon cocktails, and luxury reserves.",
        "buy_rate": 0.5,
        "items": [
            '_LVzCYVfahJF7yqdC77gxT', '_gK3VkKXD9QXCd3k8EM42p', '_UxxF3kPAjVb3kkYMLMLDN',
            '_zFMQb6pcAHLzWYMyN3g6x', '_CVBWaPP37egd4WRRjyj7W', '_rCMq1RdjjeVbFmQ9ycUkQ',
            '_1cVjGdFd8V3Q7pkad3Dt1', '_QtpdDqq1QQKXwGTJpJgUD'
        ]
    }
}

def step1_update_items():
    print("\n=== [STEP 1] Updating item_config for all 54 items ===")
    
    for i, (item_id, meta) in enumerate(ITEMS_METADATA.items()):
        item_config = {
            "stackable": meta["stackable"],
            "max_stack": meta["max_stack"],
            "consumable": meta["consumable"],
            "tradeable": meta["tradeable"],
            "rarity": meta["rarity"],
            "weight": meta["weight"],
            "value": {
                USD_ID: meta["usd"],
                CR_ID: meta["cr"]
            }
        }
        if meta.get("equip_slot"):
            item_config["equip_slot"] = meta["equip_slot"]
            
        url = f"https://app.wyvern.chat/api/worlds/lexicon/{item_id}"
        payload = {"item_config": item_config}
        
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers=get_headers(),
            method='PUT'
        )
        
        retries = 3
        while retries > 0:
            try:
                with urllib.request.urlopen(req) as resp:
                    print(f"  [{i+1}/54] Updated item_config for: {meta['name']} (${meta['usd']} / {meta['cr']} Cr)")
                    break
            except urllib.error.HTTPError as e:
                err_text = e.read().decode('utf-8', errors='ignore')
                print(f"  [ERROR] Item {item_id} ({meta['name']}): HTTP {e.code} {err_text}")
                retries -= 1
                if retries > 0:
                    time.sleep(1)
                else:
                    raise RuntimeError(f"Failed to update item {item_id}")
        time.sleep(0.1)

def step2_update_shops():
    print("\n=== [STEP 2] Configuring marketplace_config on 5 key locations ===")
    
    for loc_id, shop in SHOPS_CONFIG.items():
        inventory = []
        for item_id in shop["items"]:
            inventory.append({
                "lexicon_entry_id": item_id,
                "stock": -1,
                "restock_cycle": 24
            })
            
        marketplace_config = {
            "enabled": True,
            "name": shop["name"],
            "description": shop["description"],
            "buy_rate": shop["buy_rate"],
            "inventory": inventory
        }
        
        url = f"https://app.wyvern.chat/api/worlds/locations/{loc_id}"
        payload = {"marketplace_config": marketplace_config}
        
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers=get_headers(),
            method='PUT'
        )
        
        retries = 3
        while retries > 0:
            try:
                with urllib.request.urlopen(req) as resp:
                    print(f"  [Shop Configured] {shop['name']} at {loc_id} ({len(inventory)} items)")
                    break
            except urllib.error.HTTPError as e:
                err_text = e.read().decode('utf-8', errors='ignore')
                print(f"  [ERROR] Location {loc_id}: HTTP {e.code} {err_text}")
                retries -= 1
                if retries > 0:
                    time.sleep(1)
                else:
                    raise RuntimeError(f"Failed to update location {loc_id}")
        time.sleep(0.2)

def main():
    step1_update_items()
    step2_update_shops()
    print("\n[SUCCESS] All 54 items and 5 shop locations reconciled!")

if __name__ == '__main__':
    main()
