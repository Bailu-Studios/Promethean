from argparse import ArgumentParser
from promethean.constants import *


def entry_point():
    parser = ArgumentParser(prog=PACKAGE_NAME, description='{} CLI'.format(NAME))
    parser.add_argument('-V', '--version', help='Print {} version and exit'.format(NAME), action='store_true')

    subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')
    # start
    start = subparsers.add_parser('start', help='Start {}'.format(NAME))
    # init
    init = subparsers.add_parser('init', help='Prepare the working environment of {}. Create commonly used folders and '
                                              'generate default configuration files'.format(NAME))
    args = parser.parse_args()
