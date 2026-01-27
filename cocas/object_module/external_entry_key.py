from .attributes import Attributes

class ExternalEntryKey:
    """Describes the key for adding ExternalEntry objects to a dictionary.
    Contains the label name, attributes, sorted in non-descending order, anb
    their string representation."""
    def __init__(self, label: str, attrs: list(Attributes)):
        self.label: str = str
        self.attrs: attrs = sorted(attrs)
        self.key = str

        if len(self.attrs) > 0:
            # ATTR1 +ATTR2 ... +ATTRn
            string = " +".join(map(str, self.attrs))
            # label +ATTR1 +ATTR2 ... +ATTRn
            self.key += f"+{string}"
    
    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.key == self.key

    def __str__(self):
        return self.key
    
    def __repr__(self):
        return str(self)