from dataclasses import dataclass, field
from typing import Optional

from .symbol_attribute import SymbolAttribute
from .linkage import Linkage

@dataclass
class Entry:
    address: int
    attrs: list[SymbolAttribute] = field(default_factory=list)

    def add_linkage_attribute(self, linkage: Optional[Linkage]):
        if linkage:
            attr: Optional[SymbolAttribute] = linkage.to_attribute()
            if attr:
                self.attrs.append(attr)

    def __str__(self):
        string = ""
        if len(self.attrs) > 0:
            # ATTR1 +ATTR2 ... +ATTRn
            string = " +".join(map(str, self.attrs))
            # +ATTR1 +ATTR2 ... +ATTRn address
            return f"+{string} {self.address:02x}"
        
        return f"{self.address:02x}"
       
    def __repr__(self):
        return str(self)

