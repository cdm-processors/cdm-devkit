from dataclasses import dataclass


@dataclass
class BranchCode:
    condition: list[str]
    code: int
    inverse: list[str]
    inv_code: int


branch_codes: list[BranchCode] = [BranchCode(['eq', 'z'], 0, ['ne', 'nz', 'neq'], 1),
                                  BranchCode(['hs', 'cs', 'nlo', 'ncc'], 2, ['lo', 'cc', 'nhs', 'ncs'], 3),
                                  BranchCode(['mi', 'npl'], 4, ['pl', 'nmi'], 5),
                                  BranchCode(['vs', 'nvc'], 6, ['vc', 'nvs'], 7),
                                  BranchCode(['hi', 'nls'], 8, ['ls', 'nhi'], 9),
                                  BranchCode(['ge', 'nlt'], 10, ['lt', 'nge'], 11),
                                  BranchCode(['gt', 'nle'], 12, ['le', 'ngt'], 13),
                                  BranchCode(['r', 'anything', 'true'], 14, ['false', 'nanything'], 15)]


def check_inverse_branch(cond: str, inverse=False):
    for pair in branch_codes:
        if cond in pair.condition:
            return pair.condition[0] if not inverse else pair.inverse[0]
        elif cond in pair.inverse:
            return pair.inverse[0] if not inverse else pair.condition[0]
    else:
        return None
