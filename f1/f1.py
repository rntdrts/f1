# -*- coding: utf-8 -*-

"""f1-data.f1: provides entry point main()."""

__version__ = "0.2.0"

import sys
import argparse
from f1.actions.actions import Actions
from f1.actions.fastestlaps import FastestLap
from f1.actions.laps import Laps

def main():
    print("Executing f1 data version %s." % __version__)

    parser = argparse.ArgumentParser(
                    prog = 'f1data',
                    description = 'Transforms and presents data regarding f1 grand prix, constructors and drivers.',
                    epilog = 'Text at the bottom of help')

    parser.add_argument('actions', help='laps, fastest-laps')           # positional argument
    parser.add_argument('-gp', '--grand-prix')
    parser.add_argument('-s', '--session')
    parser.add_argument('-y', '--year')
    parser.add_argument('-o', '--out')
    parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

    args = parser.parse_args()

    if args.actions == Actions.FASTEST_LAPS.value:
        fl = FastestLap(int(args.year), args.grand_prix, args.session)
        fl.execute()
        return

    if args.actions == Actions.LAPS.value:
        fl = Laps(int(args.year), args.grand_prix, args.session)
        fl.execute()
        return
