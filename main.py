
import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_colors_data = squirrel_data["Primary Fur Color"]

squirrel_colors_dict = {
    "colors": ['gray', 'cinnamon', 'black'],
    "amount": [0, 0, 0]

}

for colors in squirrel_colors_data:
    if colors == 'Gray':
        squirrel_colors_dict['amount'][0] += 1
    elif colors == 'Cinnamon':
        squirrel_colors_dict['amount'][1] += 1
    elif colors == "Black":
        squirrel_colors_dict['amount'][2] += 1

squirrel_colors = pd.DataFrame(squirrel_colors_dict)
print(squirrel_colors)
squirrel_colors.to_csv("squirrel colors.csv")


# Teachers way...
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

