import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Disassembler for CdM Processors")

    parser.add_argument("source", type=str, nargs='?', help="source file")

    parser.add_argument('-T', '--list-targets', dest="list_targets", action="store_true",
                        default=False, help='list available targets and exit')

    parser.add_argument("-t", "--target", type=str, default="cdm16",
                        help="target processor, CdM-16 is default")

    parser.add_argument("--ivt", dest="ivt", action="store_true",
                        default=False, help="try to decode IVT")

    parser.add_argument("--fold-threshold", dest="fold_threshold", type=int, action="store",
                        default=15, help="minimal amount of repeating instructions to be folded")

    parser.add_argument("--no-fold", dest="no_fold", action="store_true",
                        default=False, help="don't fold repeating instructions")

    return parser.parse_args()


args = parse_args()
