# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# ! which python

# %%
# ! python --version

# %%
import pandas as pd
import dvc.api

# %%
with dvc.api.open(
        'data/iris.csv',
        repo='https://github.com/zachbogart/dvc_basics'
        ) as fd:
    # ... fd is a file descriptor that can be processed normally.
    
    foo = pd.read_csv(fd)

# %%
foo

# %%
