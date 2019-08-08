# File called _pytest for PyCharm compatability

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.util.testing import assert_almost_equal

from eland.tests.common import TestData


class TestDataFrameHist(TestData):

    def test_hist1(self):
        pd_flights = self.pd_flights()
        ed_flights = self.ed_flights()

        num_bins = 10

        # pandas data
        pd_distancekilometers = np.histogram(pd_flights['DistanceKilometers'], num_bins)
        pd_flightdelaymin = np.histogram(pd_flights['FlightDelayMin'], num_bins)

        pd_bins = pd.DataFrame(
            {'DistanceKilometers': pd_distancekilometers[1], 'FlightDelayMin': pd_flightdelaymin[1]})
        pd_weights = pd.DataFrame(
            {'DistanceKilometers': pd_distancekilometers[0], 'FlightDelayMin': pd_flightdelaymin[0]})

        ed_bins, ed_weights = ed_flights[['DistanceKilometers', 'FlightDelayMin']]._hist(num_bins=num_bins)

        # Numbers are slightly different
        assert_almost_equal(pd_bins, ed_bins)
        assert_almost_equal(pd_weights, ed_weights)

    def test_hist2(self):
        pd_df = self.pd_flights()[['DistanceKilometers', 'DistanceMiles', 'FlightDelayMin', 'FlightTimeHour']]
        ed_df = self.ed_flights()[['DistanceKilometers', 'DistanceMiles', 'FlightDelayMin', 'FlightTimeHour']]

        num_bins = 10

        ed_bins, ed_weights = ed_df._hist(num_bins=num_bins)

        print(ed_bins)

