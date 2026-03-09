"""This module contains structures of universal object code and debug information that is used in all other modules"""

from .concat_rsects import concat_rsects
from .external_entry import ExternalEntry
from .location import CodeLocation
from .object_module import ObjectModule, ObjectSectionRecord
from .entry import Entry, EntryKey, Linkage
from .rsects_group import RsectsGroup, group_rsects
