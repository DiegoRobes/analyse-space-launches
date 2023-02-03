import pandas as pd

df = pd.read_csv("mission_launches.csv")

del df["Unnamed: 0"]
del df["Unnamed: 0.1"]

# -------- Number of organisations and the amount of launches from each one -------- #
"""all_organisations = df["Organisation"].to_list()

clean_organisation = []
[clean_organisation.append(a) for a in all_organisations if a not in clean_organisation]

total_organisations = {"Total Number of organisations": len(clean_organisation)}

fubar = {}
for i in all_organisations:
    launches = all_organisations.count(i)
    fubar[i] = launches

launch_per_organisation = {"Organisation": [i for i in clean_organisation], "N° Launches": [i for i in fubar.values()]}

launches_df = pd.DataFrame.from_dict(launch_per_organisation)
print(launches_df)"""

# --------  Distribution of Rocket_status -------- #
"""rocket_status = df["Rocket_Status"].to_list()

status_count = {}
for i in rocket_status:
    count = rocket_status.count(i)
    status_count[i] = count

clean = []
[clean.append(x) for x in rocket_status if x not in clean]

rockets = {"Rocket": [i for i in clean], "N°": [i for i in status_count.values()]}

rocket_status_df = pd.DataFrame.from_dict(rockets)
print(rocket_status_df)"""

# --------  Outcome of missions -------- #
"""all_missions = df["Mission_Status"].to_list()

mission_status = {}
for i in all_missions:
    count = all_missions.count(i)
    mission_status[i] = count
    
status_df = pd.DataFrame.from_dict(mission_status, orient='index')
print(status_df)"""

# --------  Reported cost per mission -------- #
"""all_costs = df["Price"].to_list()
all_organisations = df["Organisation"].to_list()

report = {"Organisation": [i for i in all_organisations], "Cost per mission": [x for x in all_costs]}
report_df = pd.DataFrame.from_dict(report)
print(report_df)"""

# --------  N° of launches per country -------- #
# ("pacific ocean" is international waters. those flights where operated by zenith, the exact launch site was
# 0°N 154°W, according to wikipedia)
"""all_countries = df["Location"].to_list()

divided = []
for i in all_countries:
    big = i.split(",")
    divided.append(big)

clean = []
for i in divided:
    del i[:-1]
    for x in i:
        space = x.replace(" ", "")
        clean.append(space)

# check for special cases
for i in range(len(clean)):
    if clean[i] == 'ShahrudMissileTestSite':
        clean[i] = "Iran"
    if clean[i] == 'NewMexico':
        clean[i] = "USA"
    if clean[i] == 'YellowSea':
        clean[i] = "China"
    if clean[i] == 'PacificMissileRangeFacility':
        clean[i] = "USA"
    if clean[i] == "BarentsSea":
        clean[i] = "Russia"
    if clean[i] == 'GranCanaria':
        clean[i] = "Spain"
    if clean[i] == 'Russia':
        clean[i] = "Russian Federation"
    if clean[i] == 'NewZealand':
        clean[i] = "New Zealand"
    if clean[i] == 'NorthKorea':
        clean[i] = "North Korea"
    if clean[i] == 'SouthKorea':
        clean[i] = "South Korea"

launches_per_country = {}
for i in clean:
    launches = clean.count(i)
    launches_per_country[i] = launches

countries_dict = {"Country of Launch": [i for i in launches_per_country], "N° of Launches": [i for i in
                                                                                             launches_per_country.
                                                                                             values()]}
countries_df = pd.DataFrame.from_dict(countries_dict)
print(countries_df)
"""
