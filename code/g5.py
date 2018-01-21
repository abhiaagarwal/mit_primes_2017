from typing import List, Tuple

def geometric_median(points: List[Tuple[int, int]]):
    import numpy
    from scipy.optimize import minimize
    from scipy.spatial.distance import cdist

    points_array: numpy.array = (
        numpy.asarray(points)
    )

    def distance_sum(val: numpy.array):
        return cdist(
            [val], points_array
        ).sum()

    return minimize(
        distance_sum,
        points_array.mean(axis=0),
        method="COBYLA").x
