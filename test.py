#!/usr/bin/env python3

import investpy

df = investpy.get_funds(country='spain')
print(df)
