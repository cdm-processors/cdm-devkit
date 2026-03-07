from cocas.object_module.linkage import Linkage
from cocas.object_module.symbol_attribute import SymbolAttribute
from typing import Optional

class ExternalLabelKey:
    """Describes the key for adding ExternalEntry objects to a dictionary.
    Contains the label name, attributes, sorted in non-descending order, anb
    their string representation."""

    label: str
    attributes: set[SymbolAttribute]
    key: str

    def __init__(self, label: str,
                linkage_attr: Optional[Linkage] = None,
                attributes: Optional[list[SymbolAttribute]] = None):
        self.label = label
        self.attributes = set()
        self.key = label

        if linkage_attr:
            attr: Optional[SymbolAttribute] = linkage_attr.to_attribute()
            if attr:
                self.attributes.add(attr)
        
        if attributes:
            self.attributes.update(attributes)
        
        if len(self.attributes) > 0:
            # ATTR1 +ATTR2 ... +ATTRn
            string = " +".join(map(str, sorted(self.attributes)))
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
    
    def is_file_local(self):
        return SymbolAttribute.LOCAL in self.attributes
