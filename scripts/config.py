NAME            = "Chesss-s!"
DESC            = "1st Collectible Art Toy from CAICA & Chiangmai Local Artists. Show this NFT at CAICA booth @ CNX NFT DAY, BLOCK MOUNTAIN 2025 for Lucky Draw."
OUTPUT_PATH     = "../docs/json/{}.json"
ASSET_ENDPOINT  = 'https://bored-town.github.io/chesss/assets'

FROM_ID = 1
OUTPUT_SIZE = 10_000
RARE_RANGE = 50

NFT_DATA = {
    # common
    1: ('GINGA',              'KING',     'M.SHR'),
    2: ('BORIE IS BORING',    'QUEEN',    'BORIE'),
    3: ('SUMI BUTSU',         'BISHOP',   'DUCKZAP'),
    4: ('R0LL',               'PAWN',     'BALSAI'),
    5: ('BASE CAMP',          'KNIGHT',   'ZIINE'),
    6: ('SAP1EN',             'ROOK',     'SAP1EN'),
    # rare (1/50)
    'B': ('BORED TOWN',         'SECRET',   'BORED TOWN'),
    'G': ('GM CLUB',            'SECRET',   'GM CLUB'),
    'L': ('LUZIAX',             'SECRET',   'LUZIAX'),
}
