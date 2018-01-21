"""calculate"""



def find_matches(num: int) -> float:
    from typing import Tuple, Iterable
    sides: int = 6
    limit: int = 6

    import itertools
    combinations: Iterable[Tuple[int]] = (
        itertools.product(
            range(1, sides + 1),
            repeat=num
        )
    )

    import numpy
    matches: int = sum((
        1
        for product in (
            numpy.prod(combination)
            for combination in combinations
        )
        if product <= limit
    ))
    return matches

if __name__ == "__main__":
    import sys
    print(
        find_matches(int(sys.argv[1]))
    )
