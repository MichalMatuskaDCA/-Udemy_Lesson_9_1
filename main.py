travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
new = {}
pack = ["country", "visit", "cities"]
add_new_country = ("Russia", 2, ["Moscow", "Saint Petersburg"])
for item in range(len(pack)):
  new[pack[item]] = add_new_country[item]
  print(new)
 
travel_log.append(new)
#🚨 Do not change the code below

print(travel_log)



