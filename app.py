import pandas as pd

plans = pd.read_csv('plans.csv')
zips = pd.read_csv('zips.csv')
slcsp = pd.read_csv('slcsp.csv')

zipcode = slcsp.loc[26].zipcode
for index, row in slcsp.iterrows():
    myzips = zips[zips["zipcode"] == row.zipcode]
    rate_areas = myzips['rate_area'].tolist()
    # remove duplicates from rate areas
    rate_areas = list(dict.fromkeys(rate_areas))
    slcsp_rate = ''
    if(len(rate_areas) > 1):
        slcsp_rate = ''
    else:
        ra = rate_areas[0]
        zipcodePlans = plans[(plans["rate_area"] == ra) & (plans["metal_level"] == 'Silver')]
        noOfRows = len(zipcodePlans.index)
        if(noOfRows <= 1):
            slcsp_rate = ''
        else:
            silverRates = zipcodePlans['rate'].tolist()
            # remove duplicates from silver rates
            silverRates = list(dict.fromkeys(silverRates))
            silverRates.sort()
            slcsp_rate = format(silverRates[1], '.2f')
    slcsp.at[index, 'rate'] = slcsp_rate
print(slcsp.to_csv(index=False))

# comment this in to print out the rates into the slcsp file
# slcsp.to_csv('slcsp.csv', index=False)
