import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        shifted = z - np.max(z)
        res = np.exp(shifted)
        return np.round(res/np.sum(res),4)

        # return np.round(your_answer, 4)
        pass
