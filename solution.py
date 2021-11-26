import sys
import datetime
import pandas as pd
import numpy as np
import math
from PyQt5 import QtWidgets
from sph_filt import Ui_sphere_filtration



app = QtWidgets.QApplication(sys.argv)
sphere_filtration = QtWidgets.QWidget()
ui = Ui_sphere_filtration()
ui.setupUi(sphere_filtration)
sphere_filtration.show()


class Inpxlsx():

    def im_file(self):
        global final_data
        name = ui.lineEdit.text()
        final_data = pd.read_excel(name)
        print(name,final_data.shape)

    ui.pushButton.clicked.connect(im_file)

    def red_file(self):
        global final_data
        final_data['Alpha_i_k_0'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_1'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_2'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            2) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            2 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            2) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            2 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_3'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            3) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            3 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            3) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            3 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_4'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            4) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            4 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            4) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            4 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_5'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            5) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            5 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            5) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            5 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_6'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            6) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            6 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            6) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            6 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_7'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            7) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            7 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            7) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            7 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_8'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            8) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            8 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            8) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            8 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_9'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            9) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            9 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            9) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            9 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_10'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            10) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            10 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            10) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            10 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_11'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            11) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            11 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            11) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            11 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_12'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            12) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            12 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            12) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            12 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_13'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            13) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            13 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            13) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            13 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_14'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            14) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            14 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            14) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            14 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_15'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            15) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            15 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            15) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            15 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_1'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_2'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-2)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-2) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-2)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-2) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_3'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-3)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-3) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-3)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-3) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_4'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-4)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-4) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-4)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-4) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_5'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-5)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-5) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-5)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-5) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_6'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-6)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-6) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-6)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-6) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_7'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-7)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-7) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-7)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-7) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_8'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-8)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-8) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-8)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-8) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_9'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-9)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-9) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-9)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-9) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_10'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-10)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-10) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-10)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-10) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_11'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-11)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-11) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-11)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-11) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_12'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-12)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-12) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-12)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-12) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_13'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-13)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-13) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-13)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-13) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_14'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-14)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-14) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-14)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-14) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k_min_15'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-15)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-15) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-15)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Distance between spheres, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-15) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_k'] = final_data.apply(
            lambda x:
            x['Alpha_i_k_min_15'] + x['Alpha_i_k_min_14'] + x['Alpha_i_k_min_13'] +
            x['Alpha_i_k_min_12'] + x['Alpha_i_k_min_11'] + x['Alpha_i_k_min_10'] +
            x['Alpha_i_k_min_9'] + x['Alpha_i_k_min_8'] + x['Alpha_i_k_min_7'] +
            x['Alpha_i_k_min_6'] + x['Alpha_i_k_min_5'] + x['Alpha_i_k_min_4'] +
            x['Alpha_i_k_min_3'] + x['Alpha_i_k_min_2'] + x['Alpha_i_k_min_1'] +
            x['Alpha_i_k_0'] + x['Alpha_i_k_1'] + x['Alpha_i_k_2'] +
            x['Alpha_i_k_3'] + x['Alpha_i_k_4'] + x['Alpha_i_k_5'] +
            x['Alpha_i_k_6'] + x['Alpha_i_k_8'] + x['Alpha_i_k_10'] +
            x['Alpha_i_k_7'] + x['Alpha_i_k_9'] + x['Alpha_i_k_11'] +
            x['Alpha_i_k_12'] + x['Alpha_i_k_14'] + x['Alpha_i_k_15'] +
            x['Alpha_i_k_13']
            , axis=1)
        final_data = final_data.drop(
            ['Alpha_i_k_min_15', 'Alpha_i_k_min_14', 'Alpha_i_k_min_13', 'Alpha_i_k_min_12', 'Alpha_i_k_min_11',
             'Alpha_i_k_min_10', 'Alpha_i_k_min_9', 'Alpha_i_k_min_8', 'Alpha_i_k_min_7', 'Alpha_i_k_min_6',
             'Alpha_i_k_min_5', 'Alpha_i_k_min_4', 'Alpha_i_k_min_3', 'Alpha_i_k_min_2', 'Alpha_i_k_min_1',
             'Alpha_i_k_0', 'Alpha_i_k_1', 'Alpha_i_k_2', 'Alpha_i_k_3', 'Alpha_i_k_4', 'Alpha_i_k_5', 'Alpha_i_k_6',
             'Alpha_i_k_7', 'Alpha_i_k_8', 'Alpha_i_k_9', 'Alpha_i_k_10', 'Alpha_i_k_11', 'Alpha_i_k_12',
             'Alpha_i_k_13', 'Alpha_i_k_14', 'Alpha_i_k_15'], axis=1)
        final_data['Alpha_i_m_0'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Well radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Well radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            0 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_m_1'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Well radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Well radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            1 - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_m_min_1'] = final_data.apply(
            lambda x:

            x['Formation thickness, m'] / (x['Well radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1)) ** (2)) ** (0.5) +
            x['Formation thickness, m'] / (x['Well radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1)) ** (2)) ** (0.5) -
            x['Formation thickness, m'] / (x['Supply contour radius, m'] ** (2) +
                                           (-2 * x['Formation thickness, m'] *
                                            (-1) - 2 * x['Run to the bottom of formation, m']) ** (2)) ** (0.5)

            , axis=1)
        final_data['Alpha_i_m'] = final_data.apply(
            lambda x:
            x['Alpha_i_m_min_1'] +
            x['Alpha_i_m_0'] + x['Alpha_i_m_1']
            , axis=1)
        final_data = final_data.drop(['Alpha_i_m_0', 'Alpha_i_m_1', 'Alpha_i_m_min_1'], axis=1)
        final_data['Flow capacity'] = final_data.apply(
            lambda x:
            x['Permeabillity, mD'] *
            x['Effective thickness, meters'] / x['Oil viscosity in reservoir conditions, cP']
            , axis=1)
        final_data['Constant term'] = final_data.apply(
            lambda x:
            4 * math.pi * x['Flow capacity'] *
            x['Wellbore pressure, atm'] / x['Alpha_i_m'] - 4 * math.pi * x['Flow capacity'] *
            x['Reservoir pressure, atm'] / x['Alpha_i_m']
            , axis=1)
        final_data['alpha/alpha'] = final_data.apply(
            lambda x:
            x['Wellbore pressure, atm'] / x['Alpha_i_m']
            , axis=1)
        B = final_data['alpha/alpha'].tolist()
        C = final_data['Constant term'].tolist()
        B_min = []
        for i in B:
            B_min.append(-i)
        left_part_of_system = []
        for i in range(len(B_min)):
            copy = B_min[:]
            copy[i] += 1
            left_part_of_system.append(copy)
        A1 = np.array(left_part_of_system)
        B1 = np.array(C)
        X = np.linalg.solve(A1, B1)
        Rate = X.tolist()
        Oil_rate = []
        for i in Rate:
            Oil_rate.append(-i)

        final_data['Oil rate, m^3/day'] = Oil_rate
        final_data = final_data.drop(['Alpha_i_k', 'Alpha_i_m', 'Flow capacity', 'Constant term', 'alpha/alpha'],
                                     axis=1)
        final_data['Oil rate (surface), m^3/day'] = final_data.apply(
            lambda x:
            x['Oil rate, m^3/day'] / x['Fvf, m3/m3']
            , axis=1)
        prod = final_data['Oil rate (surface), m^3/day'].tolist()
        sum = 0
        for i in prod:
            sum += i
        ui.lineEdit_2.setText(str(sum))
        print('success')


    ui.pushButton_2.clicked.connect(red_file)

    def exp_file(self):
        global final_data

        final_data.to_excel('solution.xlsx',index=False)

    ui.pushButton_3.clicked.connect(exp_file)


sys.exit(app.exec_())
