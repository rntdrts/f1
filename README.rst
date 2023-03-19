f1 command line
========================

This is a command line project for retrieving f1 data in different data outputs.


Usage
-----

The project is built around actions.

Behavior
--------

For now it only supports an argument, for actions, and it only support the following ones:
    laps
    fastest-laps

There is required parameters, to run the command:
    -gp = grand-prix
    -y = year
    -s = session

The project is now creating predefined fields on the folder `/output` with csv files.

Development installation
--------
Information on built and how to use in develop mode.
The project has been built and tested using python 3.11.

Install dependencies
*******************
    $ pip install

Build CLI
*******************
    $ python setup.py develop
    $ f1 laps -gp "Saudi Arabian Grand Prix" -y 2023 -s "FP1"

Run in dev mode
**************************************
    $ ./f1-runner.py laps -gp "Saudi Arabian Grand Prix" -y 2023 -s "Q"
