import argparse

def parse() -> dict:
    """parse command-line arguments or use default arguments if none are given."""
    parser = argparse.ArgumentParser()

    # create necessary argument (directory to parse)
    parser.add_argument("image", help="the image file to evaluate")

    # use the parsed arguments
    args = parser.parse_args()

    # print
    print(f"Evaluating {args.image}...")

    # convert to dictionary and return
    args_dict = vars(args)
    return args_dict
