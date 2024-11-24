# %% Setup
from os import chdir, path
from pathlib import Path
from pyrosm import get_data, OSM

chdir(Path(path.realpath("__file__")).parents[0].parents[0])

# %% Init
fp = get_data("Moscow", directory=".cache", update=False)
osm = OSM(fp)

# %% Process
custom_filter = {"shop": True}
pois = osm.get_pois(custom_filter=custom_filter)

# %% Analzye
buildings = osm.get_buildings()
buildings.plot()
