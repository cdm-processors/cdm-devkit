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

    return parser.parse_args()


args = parse_args()
