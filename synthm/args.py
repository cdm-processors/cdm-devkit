import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Secondary Decoder Synthesis Utility')

    parser.add_argument('-d', dest='debug', action='store_true', default=False,
                        help="provide verbose output for debugging")
    parser.add_argument('-bw', dest='color', action='store_false', default=True, help="monochrome output")
    parser.add_argument('-i', dest='gen_image', action='store_true', default=False, help="generate ROM image")
    parser.add_argument('-f', dest='fill', type=str, default='0', help="value to fill")
    parser.add_argument('defs', type=str, help="secondary decoder definition file")

    return parser.parse_args()
