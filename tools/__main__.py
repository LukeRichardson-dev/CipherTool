from affine import Affine, AffineKeyContext
from shared.frequency import EXAMPLE_2, EXAMPLE



for a in range(0, 26):
    for b in range(26):
      
        aff = Affine(AffineKeyContext(a, b))

        if a == 0:
            continue

        if Affine.inv_mod(a, 26) is None:
            continue

        res: str = aff.apply(EXAMPLE_2[:6])

        if res[:4] == "DEAR":
            print(aff.apply(EXAMPLE_2), a, b)
