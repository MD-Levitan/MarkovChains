import Algorithms as alg
from CMM import CMM
from CMM_S import CMM_S
import matplotlib.pyplot as plt
import numpy as np


class Estimation:

        """
        L - length
        """

        def __init__(self, model, l_max=1000, k_max=1000):
            self.model = model
            self.L_max = l_max
            self.K_max = k_max
            self.sample = Estimation.generate_sample(self.model, self.L_max,
                                                    self.K_max)

        @staticmethod
        def generate_sample(model, l_max, k_max):
            sample = [[alg.generate_CMM(model.N, model.Pi, model.P, l) for _ in range(0, k_max)] for l in range(0, l_max)]
            return sample

        @staticmethod
        def norm(ar1, ar2):
            return np.linalg.norm((ar1 - ar2), ord='fro')

        def standard_deviation(self, l, k, param='P'):
            if 0 <= k < self.K_max and 0 <= l < self.L_max:
                estimation_model = alg.estimation_model(self.sample[l][k], self.model)
                if param == 'P':
                    std_deviation = Estimation.norm(estimation_model.P, self.model.P)
                if param == 'Pi':
                    std_deviation = Estimation.norm(estimation_model.Pi, self.model.Pi)
            return std_deviation

        def estimation_deviation(self, l):
            if 0 <= l < self.L_max:
                return sum(self.standard_deviation(l, k) for k in range(0, self.K_max))/self.K_max

        def graphic(self, step=5):
            std = [self.estimation_deviation(l) for l in range(0, self.L_max)]
            fig, ax = plt.subplots()
            plt.title("")

            ax.plot(range(0, self.L_max), std)

            ax.set_xticks(np.arange(0, self.L_max, step))
            ax.set_yticks(np.arange(0, 1., 0.1))

            ax.set_xlabel("T")
            ax.set_ylabel("std(T)")
            plt.grid()
            plt.show()



cmm = CMM()

est = Estimation(cmm, 80, 50)
est.graphic()
