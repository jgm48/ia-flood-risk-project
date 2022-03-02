#Task 2G
from floodsystem.analysis import risk_level_towns, risk_level_stations

def run():
    """Requirements for task 2G"""
    severe, high, moderate, low = risk_level_towns()
    print("Severe level risk towns are: {}".format(severe))
    print("High level risk towns are: {}".format(high))
    print("Moderate level risk towns are: {}".format(moderate))
    print("Low level risk towns are: {}".format(low))

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
# takes a v long time to produce the output