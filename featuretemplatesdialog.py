# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4 import uic
import os

basepath = os.path.dirname(__file__)
uipath = os.path.join(basepath,'ui_featuretemplates.ui')
widgetForm, baseClass = uic.loadUiType(uipath)

class FeatureTemplatesWidget(baseClass, widgetForm):
    def __init__(self, parent=None):
        super(FeatureTemplatesWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        
    def setModel(self, model):
        self.treeTemplates.setModel(model)
