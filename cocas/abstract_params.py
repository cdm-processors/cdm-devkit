import abc


class TargetParamsInterface(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def name():
        pass

    @staticmethod
    @abc.abstractmethod
    def max_entry_size() -> int:
        pass

    @staticmethod
    @abc.abstractmethod
    def default_alignment() -> int:
        pass

    @staticmethod
    @abc.abstractmethod
    def object_file_header() -> str:
        pass
