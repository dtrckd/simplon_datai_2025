#!/usr/bin/python

import json
import os
from pprint import pprint
from typing import List, Union

import numpy as np
import openai
import pandas as pd
import requests
from bs4 import BeautifulSoup

openai.api_key = os.environ["OPENAI_API_KEY"]

if __name__ == "__main__":

    # Save the results
    with open("results.json") as f:
        links = json.load(f)

    # re-order with descendant simililarities

    # with df
    df = pd.DataFrame(links)
    df = df.sort_values("sim", ascending=False)
    print(df)
