from cocas.targets import TargetParamsInterface


class TargetParams(TargetParamsInterface):
    @staticmethod
    def name():
        return 'CdM-8'

    @staticmethod
    def max_entry_size() -> int:
        return 1

    @staticmethod
    def default_alignment() -> int:
        return 1

    @staticmethod
    def object_file_header() -> str:
        return ''
