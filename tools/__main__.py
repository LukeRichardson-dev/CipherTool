from affine import Affine, AffineKeyContext
from shared.frequency import EXAMPLE_2, EXAMPLE
from affine import inv_mod

aff = Affine()

for a in range(0, 26):
    for b in range(26): 
        if a == 0:
            continue

        if inv_mod(a, 26) is None:
            continue

        res: str = aff.apply(EXAMPLE[:6], AffineKeyContext(a, b))[0]
        if res[:3] == "DEA":
            print(aff.apply(EXAMPLE[:], AffineKeyContext(a, b))[0], a, b)