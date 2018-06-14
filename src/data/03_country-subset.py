#!/usr/bin/env python


import sys
import datetime

import pandas as pd


def get_country(filename, country):
    # Load table
    wine = pd.read_csv(filename)

    # Use the country name to subset data
    subset_country = wine[wine['country'] == country ].copy()

    # Constructing the fname
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    fname = f'data/processed/{today}-winemag_{country}.csv'

    # Saving the csv
    subset_country.to_csv(fname)
    print(fname)  # print the fname from here

    return(subset_country)  #returns the data frame

def get_mean_price(filename):
    """ function to get the mean price of the wines
    rounded to 4 decimals"""
    wine = pd.read_csv(filename)
    mean_price = wine['price'].mean()
    return round(mean_price, 4)  # note the rounding here


if __name__ == '__main__':
    filename = sys.argv[1]
    country = sys.argv[2]
    print(f'Subsetting: {filename}')
    print(f'Country searched: {country}')

    print(get_country(filename, country))
