# -*- coding: utf-8 -*-

def classFactory(iface):
    # load FeatureTemplates class from file FeatureTemplates
    from featuretemplates import FeatureTemplates
    return FeatureTemplates(iface)
