'''
Created on Aug 11, 2013

@author: nathan.woodrow
'''

from unittest import TestCase
from model import FeatureTemplatesModel
from PyQt4.QtCore import Qt

class FeatureTemplateModelTest(TestCase):
    def test_data_returns_name_for_display(self):
        template = {"name" : "Test"}
        model = FeatureTemplatesModel(templates=[template])
        index = model.createIndex(0,1)
        name = model.data(index, Qt.DisplayRole)
        self.assertEqual(name, "Test")