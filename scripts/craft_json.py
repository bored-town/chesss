from config import *
from common import *
from pprint import pprint as pp
import json

common = BalancedShuffler([ 1, 2, 3, 4, 5, 6 ])
rare = BalancedShuffler([ 'B', 'G', 'L' ])
chunk = [ common.get_next() for i in range(0, OUTPUT_SIZE) ]

# add rare
for i in range(0, OUTPUT_SIZE, RARE_RANGE):
    pick = i + random.randint(0, RARE_RANGE-1)
    chunk[pick] = rare.get_next()

# debug
#for i, d in enumerate(chunk):
#    print(d, end='\n' if (i+1) % RARE_RANGE == 0 else ' ')

for i in range(0, OUTPUT_SIZE):
    token_id = i + FROM_ID
    dest = OUTPUT_PATH.format(token_id)
    [title, chess, artist] = NFT_DATA[chunk[i]]

    # craft data
    data = {
        "name": "{} #{}".format(NAME, token_id),
        "description": DESC,
        "image": "{}/nft_preview_{}.png".format(ASSET_ENDPOINT, title),
        "animation_url": "{}/{}.mov".format(ASSET_ENDPOINT, title),
        "attributes": [
            {
                "trait_type": "CHESS",
                "value": chess,
            },
            {
                "trait_type": "ARTIST",
                "value": artist,
            },
        ],
    }

    # write file
    print(dest)
    #pp(data)
    with open(dest, "w") as f:
        json.dump(data, f)
