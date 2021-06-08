import argparse
import importlib.util
import logging
import os
import sys
from Tests import tests_runner

from Factory.choose_serializer import ChooseSerializer


logging.basicConfig(
    format="%(message)s",
    level=logging.INFO
)


def create_serializer(info_type):
    serializer = ChooseSerializer.choose(info_type)
    return serializer


def main():
    parser = argparse.ArgumentParser(description='Serializer')
    parser.add_argument('--source',
                        default=None,
                        type=str,
                        help="path of source python module;")
    parser.add_argument('--name',
                        default=None,
                        type=str,
                        help="name of object you want to serialize;")
    parser.add_argument('--serializer',
                        default='json',
                        type=str,
                        help="choose serializer [json/toml/yaml/pickle];")
    parser.add_argument('--indent',
                        default=0,
                        type=int,
                        help="number of spaces for indents;")
    parser.add_argument('-s',
                        '--sort',
                        const=True,
                        action='store_const',
                        help="enable sorting keys;")
    parser.add_argument('-f',
                        '--file',
                        default=None,
                        type=str,
                        help="path of file to save;")
    parser.add_argument('-ht',
                        '--hidetest',
                        const=True,
                        action='store_const',
                        help="hide output tests to console;")
    parser.add_argument('-hr',
                        '--hideresult',
                        const=True,
                        action='store_const',
                        help="hide output to console;")
    parser.add_argument('-e',
                        '--exec',
                        const=True,
                        action='store_const',
                        help="deserialization and print result of execution.")
    args = parser.parse_args()

    if args.source is None:
        logging.info('No source file path!')
        return

    if args.name is None:
        logging.info('No object to serialize and deserialize!')
        return

    if args.serializer is None:
        logging.info('Incorrect serializer!')
        return

    try:
        sys.stdout = open(os.devnull, 'w')
        spec = importlib.util.spec_from_file_location("temp", args.source)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        sys.stdout = sys.__stdout__
    except AttributeError:
        logging.info(str(args.source) + " not found!")
        return

    try:
        cur = getattr(foo, args.name)
        serializer = create_serializer(args.serializer)
        result = serializer.dumps(cur, args.indent, args.sort)

        if not args.hideresult:
            logging.info(result)

        if not args.hidetest:
            logging.info(tests_runner.run_tests())

        if args.file is not None:
            serializer.dump(cur, args.file, args.sort, args.indent)
    except AttributeError:
        logging.info(args.name + " not found in " + args.source + "!")


if __name__ == "__main__":
    main()
