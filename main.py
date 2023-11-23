
# with open(".\Angelia\Day_25_WeatherData_CSV\weather_data.csv") as file:
#     data=file.readlines()
# print()



# import csv

# with open("Angelia\Day_25_WeatherData_CSV\weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#     #print(data)


# import pandas

# temperature=[]
# data = pandas.read_csv("Angelia\Day_25_WeatherData_CSV\weather_data.csv")
# # temperature=data["temp"]
# # print(temperature)

# max_temp=data["temp"].max()
# print(max_temp)
# print(data[data.temp==max_temp])

import pandas
data=pandas.read_csv("C:\\python\\Angelia\\WeatherData_CSV\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur Color" :["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]


}
df=pandas.DataFrame(data_dict)
df.to_csv("C:\\python\\Angelia\\WeatherData_CSV\\Squirrel_count.csv")