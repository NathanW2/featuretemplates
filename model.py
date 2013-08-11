from PyQt4.QtCore import QAbstractItemModel, QModelIndex, Qt

class FeatureTemplatesModel(QAbstractItemModel):
    def __init__(self, templates=None, parent=None):
        super(FeatureTemplatesModel, self).__init__(parent)
        self.templates = templates or []
        
    def columnCount(self, parent = QModelIndex()):
        return 1
    
    def rowCount(self, parent = QModelIndex()):
        return len(self.templates)
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.templates[index.row()]['name']
        
        return None
    
    def hasChildren(self, index):
        return True
    
    def index(self, row, column, parent = QModelIndex()):
        if parent.isValid() and not parent.column() == 0:
            return QModelIndex()
        
        item = self.templates[row]
        if item:
            return self.createIndex(row, column, item)
        else:
            return QModelIndex()
        
        
        
#         
# Template
#     Name
#     Attributes
#     Group
#     