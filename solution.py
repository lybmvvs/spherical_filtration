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


class Inpxlsx():

    def im_file(self):

        name = ui.textEdit.text()
        #final_data = pd.read_excel(file_name)
        print(name)

    ui.pushButton.clicked.connect(im_file)


sys.exit(app.exec_())
