# Tier A: direct spellings / variants of the seed concept
TIER_A = {
    "merchant", "merchants",
    "marchant", "marchants"
}

# Tier B: closely related commercial roles / terms
TIER_B = {
    "factor", "chapman",
    "adventurer", "adventurers",
    "venturer", "venturers",
    "staple", "staplers",
    "trade",
    "purser"
}

# Tier C: "maybe" occupational neighborhood (often adjacent, not always merchant-specific)
TIER_C = {
    "clothier", "clothyer",
    "tailor", "tayler",
    "haberdasher",
    "goldsmith",
    "vintner",
    "brewer",
    "banker",
    "grazier",
    "jeweller"
}

print("Tier A size:", len(TIER_A))
print("Tier B size:", len(TIER_B))
print("Tier C size:", len(TIER_C))

print("\nTier A:", sorted(TIER_A))
print("\nTier B:", sorted(TIER_B))
print("\nTier C:", sorted(TIER_C))