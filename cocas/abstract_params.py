import abc


class TargetParamsInterface(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def max_entry_size() -> int:
        pass

    @staticmethod
    @abc.abstractmethod
    def default_alignment() -> int:
        pass
