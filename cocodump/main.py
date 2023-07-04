from pathlib import Path

from cocodump.args import args, parse_args
from cocodump.reader import read_img
from cocodump.target_loader import import_target_decoder, list_target_decoders


def main():
    parse_args()

    available_targets = list_target_decoders()

    if args.list_targets:
        print(f"Available targets: {', '.join(available_targets)}")
        exit(0)

    if args.target not in available_targets:
        print(f"Ivalid target: {args.target}")
        print(f"Available targets: {', '.join(available_targets)}")
        exit(1)

    decoder = import_target_decoder(args.target)

    if args.source is None:
        print("No files provided!")
        exit(0)

    raw_bytes = read_img(Path(args.source))

    decoded_bytes = decoder.decode(raw_bytes)

    decoded_bytes.place_labels()

    for inst in decoded_bytes.to_instructions():
        print(inst.emit())


if __name__ == "__main__":
    main()