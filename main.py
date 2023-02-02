import pandas as pd

df = pd.read_csv("mission_launches.csv")

del df["Unnamed: 0"]
del df["Unnamed: 0.1"]

# -------- Number of organisations and the amount of launches from each one -------- #
"""all_organisations = df["Organisation"].to_list()

clean_organisation = []
[clean_organisation.append(a) for a in all_organisations if a not in clean_organisation]

total_organisations = {"Total Number of organisations": len(clean_organisation)}
print(total_organisations)

launch_per_organisation = {}

for i in all_organisations:
    launches = all_organisations.count(i)
    launch_per_organisation[i] = launches

print(launch_per_organisation)"""

# --------  Distribution of Rocket_status -------- #
"""rocket_status = df["Rocket_Status"].to_list()
print(len(rocket_status))

status_count = {}
for i in rocket_status:
    count = rocket_status.count(i)
    status_count[i] = count
print(status_count)
"""

# --------  Reported cost per mission -------- #
"""all_costs = df["Price"].to_list()
reported = [i for i in all_costs if str(i) != "nan"]

all_missions = {"total_missions": len(all_costs), "missions_w_reported_cost": len(reported)}
print(reported)
print(all_missions)"""


# --------  N° of launches per country -------- #
# ("pacific ocean" is international waters. those flights where operated by zenith, the exact launch site was
# 0°N 154°W, according to wikipedia)
all_countries = df["Location"].to_list()

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

print(launches_per_country)

# ask pandas to find every success and failure row, and then give you the content of the LOCATION cell of every row.
# you want: "location": Success, "location": failure, etc.
# then divide in 2 separate dictionaries: successes per country, failures per country

