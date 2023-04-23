import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Secondary Decoder Synthesis Utility')

    parser.add_argument('-d', dest='debug', action='store_true', default=False,
                        help="provide verbose output for debuggig")
    parser.add_argument('-bw', dest='color', action='store_false', default=True, help="monocrome output")
    parser.add_argument('-i', dest='gen_image', action='store_true', default=False, help="generate ROM image")
    parser.add_argument('defs', type=str, help="secondary decoder definition file")

    return parser.parse_args()
