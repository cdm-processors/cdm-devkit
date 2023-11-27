from cocas.abstract_params import TargetParamsInterface


class TargetParams(TargetParamsInterface):
    @staticmethod
    def name():
        return 'CdM-16'

    @staticmethod
    def max_entry_size() -> int:
        return 2

    @staticmethod
    def default_alignment() -> int:
        return 2

    @staticmethod
    def object_file_header() -> str:
        return 'CDM16'
