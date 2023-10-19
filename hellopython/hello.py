from argparse import ArgumentParser
import numpy as np


def dummy_print_hello() -> int:
    parser = ArgumentParser(description="Process the BL index file for the relevant files to download")
    print("Duff Description: {}".format(parser.description))
    x = np.random.uniform()
    print("Numpy says: {}".format(x))
    return 0
