import pandas as pd
import requests
import json
from datetime import datetime
import time
import math
import numpy as np
import streamlit as st

baseUrl = 'https://api.llama.fi'
chainName = "arbitrum"
dexOverviewByChain = requests.get(baseUrl + '/overview/dexs/' + chainName +
                                  '?excludeTotalDataChart=false' +
                                  '&excludeTotalDataChartBreakdown=false' +
                                  '&dataType=dailyVolume')

dexOverviewByChain.json().keys()
protocol_dicts = dexOverviewByChain.json()['protocols']
protocol_dicts

namelist = []
for dict in range(len(protocol_dicts)):
  for key in protocol_dicts[dict]:
    if key == 'name':
      print(protocol_dicts[dict][key])
      namelist.append(protocol_dicts[dict][key])


change_1d_list = []
for dict in range(len(protocol_dicts)):
  for key in protocol_dicts[dict]:
    if key == 'change_1d':
      print(protocol_dicts[dict][key])
      change_1d_list.append(protocol_dicts[dict][key])


vol_dict = {"names": namelist, '1d Volumes': change_1d_list }
vol_df = pd.DataFrame(vol_dict)

st.title("Arbitrum top 5 dex's by volume", anchor="arbitrum_analytics")


st.write(vol_df)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)