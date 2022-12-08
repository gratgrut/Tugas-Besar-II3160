import json


with open("heart.json", "r") as read_file:
    hearts = json.load(read_file)


for heart in hearts:
        if heart.get('id') == 5:
            print(heart)