import sys
import datetime
import pandas as pd
import numpy as np
import math
from PyQt5 import QtWidgets
from sphere_filt import Ui_sphere_filtration



app = QtWidgets.QApplication(sys.argv)
sphere_filtration = QtWidgets.QWidget()
ui = Ui_sphere_filtration()
ui.setupUi(sphere_filtration)
sphere_filtration.show()




sys.exit(app.exec_())
