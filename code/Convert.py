# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
from fls import *
from itertools import chain

# # Convert Keys

# +
TARGETS = [
 'MBA21',
 'MBA20',
 'Surface21',
 'iPadPro21',
 'iPadPro',
 'iPadBea',
 'iPhone20',
]

APPS = [
    'ssh', 
    'Working Copy', 
    'Blink', 
    #'Termius',
]
# -

SRCDIR = "../source"
OUTDIR = "../out"
KEYFN = "Public Keys.xlsx"
OUTFN = "Authorized Keys"

df0 = pd.read_excel(join(SRCDIR, KEYFN))
df0

apps = list(df0["App"])
apps

targets = list(df0)[1:]
targets

df = df0.set_index("App")
df = df.filter(APPS, axis=0)
df = df.filter(TARGETS, axis=1)
df = df.fillna("")
df

df_dct = df.to_dict()
df_dct["MBA21"]

keys = [[ky for _, ky in dct.items()] for _, dct in df_dct.items()]
keys = list(k for k in chain(*keys) if k)
#keys

keys_str = "\n\n".join(keys)
print(keys_str)

fsave(keys_str, OUTFN, OUTDIR)

help (fsave)


