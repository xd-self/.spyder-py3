# -*- coding: utf-8 -*-
"""
identify out replicates from a series!
"""

import pandas as pd

ser_idx = pd.value_counts(ser) > 1
reps = ser_idx.index[ser_idx.values == True]
reps = pd.Series(reps)