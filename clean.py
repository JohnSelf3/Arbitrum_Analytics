import json
import pandas as pd
from os import read


class Protocol:

  name: str="default"
  daily: float
  weekly: float
  monthly: float

  def __init__(
    self, name="", daily=0, weekly=0, monthly=0):

    self.name = name
    self.daily = daily
    self.weekly = weekly
    self.monthly = monthly
  
  def __str__(self) -> str:
    return f"{{ name: {self.name}, daily: {self.daily} }}"

  def dailyDiff(self):
    return (self.monthly / 30) - self.daily

def defiLlamaDataToProtocols(data: str, toDf=True) -> list[Protocol]|pd.DataFrame:
  #that's just taking raw json data and parsing it into a python dict.
  raw = json.loads(data)
  if (not raw or "protocols" not in data):
    print("no data passed to function")
    return []

  raw = raw["protocols"]
  names = list(map(lambda p: p["name"], raw))
  daily = list(map(lambda p: p["total24h"], raw))
  weekly = list(map(lambda p: p["total7d"], raw))
  monthly = list(map(lambda p: p["total30d"], raw))

  if (not toDf):
    protocols: list[Protocol] = []
    for i in range(len(names)):
      protocols.append(Protocol)
        name=names[i], daily=daily[i], weekly=weekly[i], monthly=monthly[i]
      ))
    protocols[0].dailyDiff()
    return protocols

  return pd.DataFrame({
    "name": names,
    "daily": daily,
    "weekly": weekly,
    "monthly": monthly,
  })
  
if __name__ == "__main__":
  with open("./data/arb-dexs-sample.json") as f:
    protocols: pd.DataFrame = defiLlamaDataToProtocols(f.read(), toDf=True)
    print(protocols.head())


