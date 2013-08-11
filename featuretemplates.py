# -*- coding: utf-8 -*-


# Import the PyQt and QGIS libraries
from PyQt4.QtCore import QSettings, QTranslator, QCoreApplication, qVersion, Qt
from PyQt4.QtGui import QAction, QIcon, QDockWidget

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from featuretemplatesdialog import FeatureTemplatesWidget
from model import FeatureTemplatesModel
import os.path


class FeatureTemplates:

    def __init__(self, iface):
        self.iface = iface
        self.dock = None
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 
                                  'i18n', 
                                  'featuretemplates_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        self.action = QAction(QIcon(":/plugins/featuretemplates/icon.png"),
                              u"Feature Templates", 
                              self.iface.mainWindow())

        self.action.triggered.connect(self.show_dock)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&FeatureTemplates", self.action)

    def unload(self):
        self.iface.removePluginMenu(u"&FeatureTemplates", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        if self.dock:
            self.iface.removeDockWidget(self.dock)

    def show_dock(self):
        if not self.dock:
            self.dock = QDockWidget('Feature Templates', self.iface.mainWindow())
            self.widget = FeatureTemplatesWidget(self.dock)
            template = {'name' : 'Test'}
            self.model = FeatureTemplatesModel(templates=[template])
            self.widget.setModel(self.model)
            self.dock.setWidget(self.widget)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        
        self.dock.show()
