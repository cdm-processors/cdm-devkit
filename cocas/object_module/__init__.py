"""This module contains structures of universal object code and debug information that is used in all other modules"""

from .concat_rsects import concat_rsects
from .external_entry import ExternalEntry
from .location import CodeLocation
from .object_module import ObjectModule, ObjectSectionRecord
from .linkage import Linkage
from .attributes import Attributes
from .entry import Entry
