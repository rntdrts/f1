import matplotlib.pyplot as plt
import pandas as pd
from timple.timedelta import strftimedelta
import fastf1
import fastf1.plotting
from .action import Action
from .actions import Actions

# -*- coding: utf-8 -*-
class Laps(Action):
  def __init__(self, year, circuit, session):
    super().__init__(year, circuit, session, Actions.LAPS.value)
    self.year = year
    self.circuit = circuit
    self.session = session

  def execute(self):
    fastf1.Cache.enable_cache('./f1/cache')  # replace with your cache directory

    # enable some matplotlib patches for plotting timedelta values and load
    # FastF1's default color scheme
    fastf1.plotting.setup_mpl()

    # load a session and its telemetry data
    session = fastf1.get_session(self.year, self.circuit, self.session)
    session.load()

    drivers = pd.unique(session.laps['Driver'])

    self.writeToCsv('Driver, LapTime, Sector1Time, Sector2Time, Sector3Time, Tire Compound, Tyre Life, FreshTyre, Stint')
    for drv in drivers:
        drvs_laps = session.laps.pick_driver(drv)

        for _, lap in drvs_laps.iterrows():
          self.printLap(lap)
