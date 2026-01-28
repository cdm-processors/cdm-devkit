from ..object_module.linkage import Linkage
from ..object_module.attributes import Attributes
from typing import Optional

class ExternalLabelKey:
    """Describes the key for adding ExternalEntry objects to a dictionary.
    Contains the label name, attributes, sorted in non-descending order, anb
    their string representation."""
    def __init__(self, label: str, linkage_attr: Optional[Linkage] = None):
        self.label: str = label
        self.attrs: list(Attributes) = []
        self.key: str = label

        if linkage_attr:
            attr: Attributes = linkage_attr.to_attribute()
            if attr != Attributes.NONE:
                self.attrs.append(linkage_attr.to_attribute())

        if len(self.attrs) > 0:
            # ATTR1 +ATTR2 ... +ATTRn
            string = " +".join(map(str, self.attrs))
            # label +ATTR1 +ATTR2 ... +ATTRn
            self.key += f" +{string}"
    
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