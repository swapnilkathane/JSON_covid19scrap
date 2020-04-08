#import json
import requests
city=[]
cases=[]
#city = input("Enter city name to find coronavirus data")
url='https://api.covid19india.org/state_district_wise.json'
response = requests.get(url)
d= response.json()
for i,j in d.items():
    for k,l in j.items():
       # print(k,l)
        for m,n in l.items():
            #print(i)
            for o,t in n.items():
                if(o =='confirmed' and i=='Maharashtra'):
                    city.append(m)
                    cases.append(t)

import pandas
dict={'City Name': city , 'Confirmed Cases' : cases}

df=pandas.DataFrame(dict)

df.to_csv('coronadata.csv')

import matplotlib.pyplot as plt

plt.plot(city,cases)

plt.xlabel('city')
plt.xticks(rotation=60)
plt.ylabel('cases')
plt.title('Corona analysis in mahrashtra')
plt.show()
