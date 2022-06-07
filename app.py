import pandas as pd

plans = pd.read_csv('plans.csv')
zips = pd.read_csv('zips.csv')
slcsp = pd.read_csv('slcsp.csv')

zipcode = slcsp.loc[26].zipcode
for index, row in slcsp.iterrows():
    zipcode = row.zipcode
    myzips = zips[zips["zipcode"] == zipcode]
    rate_areas = myzips['rate_area'].tolist()
    # remove duplicates
    rate_areas = list(dict.fromkeys(rate_areas))
    for ra in rate_areas:
        zipcodePlans = plans[(plans["rate_area"] == ra) & (plans["metal_level"] == 'Silver')]
        print("no. of zipcode plans: ", len(zipcodePlans.index))
        silverRates = zipcodePlans['rate'].tolist()
        print('silver rates: ', len(silverRates))
# theRateArea = myzips.iloc[0].rate_area
# print('theRateArea: ', theRateArea)
# for index, row in myzips.iterrows():
#     if(row.loc["rate_area"] != theRateArea):
#         print(f'zipcode ${zipcode} has multiple rate areas in zips.csv: ${theRateArea} and ${row.loc["rate_area"]}')
