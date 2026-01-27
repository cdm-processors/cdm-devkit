from dataclasses import dataclass

from .attributes import Attributes
from .linkage import Linkage

@dataclass
class Entry:
    def __init__(self, address: int, linkage: Linkage):
        self.address: int = address
        self.attrs: list(Attributes) = list()
        match linkage:
            case Linkage.FILE_LOCAL:
                self.attrs.append(Attributes.LOCAL)
            case Linkage.WEAK_GLOBAL:
                self.attrs.append(Attributes.WEAK)
            case _:
                pass
    
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

