import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model.iris_model import IrisModel 
from model.police import Police



if __name__ == "__main__":
    iris = IrisModel()
    iris.draw_scatter()
    iris.draw_errors()

    iris.draw_adaline_graph()
    iris.plot_decision_regions()
    