from cocas.abstract_params import TargetParamsInterface


class TargetParams(TargetParamsInterface):
    @staticmethod
    def max_entry_size() -> int:
        return 2

    @staticmethod
    def default_alignment() -> int:
        return 2
