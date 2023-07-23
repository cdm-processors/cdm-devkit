from pathlib import Path

from cocodump.args import parse_args
from cocodump.asm_emitter import emit_asm
from cocodump.reader import read_img
from cocodump.target_loader import import_target_decoder, list_target_decoders, normalize_target_name


def main():
    args = parse_args()

    available_targets = list_target_decoders()

    target = normalize_target_name(args.target)

    if args.list_targets:
        print(f"Available targets: {', '.join(available_targets)}")
        exit(0)

    if target not in available_targets:
        print(f"Invalid target: {target}")
        print(f"Available targets: {', '.join(available_targets)}")
        exit(1)

    decoder = import_target_decoder(target)

    if args.source is None:
        print("No files provided!")
        exit(0)

    raw_bytes = read_img(Path(args.source))

    decoded_section = decoder.decode(raw_bytes, args.ivt)

    decoded_section.place_labels()

    emit_asm(decoded_section, not args.no_fold, args.fold_threshold, args.colored)


if __name__ == "__main__":
    main()
