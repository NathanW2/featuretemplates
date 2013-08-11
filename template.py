class Template(object):
    def __init__(self, name, attributes, geometry_type):
        self.attributes = attributes
        self.geometry_type = geometry_type
        self.name = name
        self._moredetails = False
        
    @property
    def more_details_needed(self):
        return self._moredetails
    
    @more_details_needed.setter
    def more_details_needed(self, value):
        self._moredetails = value
