import importlib
import pandas as pd
import numpy.testing as npt
import pandas.testing as pdt

country = importlib.import_module('.data.03_country-subset', 'src')

interim_data = "data/interim/2018-06-14-winemag_priceGBP.csv"
processed_data = "data/processed/2018-06-14-winemag_Chile.csv"


def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    
    assert mean_price == 20.7865
    npt.assert_allclose(country.get_mean_price(processed_data),
                                    20.787, rtol = 0.01)

def test_get_country():
    # call the function
    df = country.get_country(interim_data, 'Chile')

    # load my previous dataset
    base = pd.read_csv(processed_data)
    
    # check if I am getting a dataframe
    assert isinstance(df, pd.DataFrame)
    assert isinstance(base, pd.DataFrame)

    # check that they are the same dataframes
    pdt.assert_frame_equal(df, base)
    
    
    