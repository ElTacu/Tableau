import sys
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

df = pd.read_csv("C:/Users/djimenez/Desktop/visual/steve_tip/{}.csv".format(sys.argv[1]))

df["Project Type"].loc[df["Project Type"] == "Bike/Ped"] = "Bike & Pedestrian"
df["Project Type"].loc[df["Project Type"] == "Capacity Proj"] = "Roadway Capacity"
df["Project Type"].loc[df["Project Type"] == "Hwy & Brg Pres"] = "Highway & Bridge Preservation"
df["Project Type"].loc[df["Project Type"] == "ITS-TSM"] = "Operational & Performance Management"
df["Project Type"].loc[df["Project Type"] == "Misc"] = "Miscellaneous"
df["Project Type"].loc[df["Project Type"] == "TDM"] = "Travel Demand Management"
df["Funding Source"][df["Funding Source"].str.contains("Federal")] = "Federal"
df["Lead Agency"].loc[df["Lead Agency"] == "Albuq. Public Schools"] = "Albuquerque Public Schools"
df.to_csv("tip_latest.csv",index = False)