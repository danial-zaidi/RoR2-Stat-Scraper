import easyocr
import pandas as pd
import os

def rename_screenshots(directory):
    files = os.listdir(directory)

    pair_counter = 1
    image_counter = 1

    for filename in files:
        if filename.endswith('.png'):
            new_filename = f"pair_{pair_counter:02d}_{image_counter:02d}.png"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            
            image_counter += 1
            if image_counter > 2:
                image_counter = 1
                pair_counter += 1



def pngreader(directory):
    files = os.listdir(directory)
    
    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

    result = reader.readtext('a1.png',adjust_contrast=0.1, detail = 0)
    result2 = reader.readtext('a2.png',adjust_contrast=0.1, detail = 0)
    
    for pictures in files:
        result[0]


    return result


# reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

# result = reader.readtext('a1.png',adjust_contrast=0.1, detail = 0)
# result2 = reader.readtext('a2.png',adjust_contrast=0.1, detail = 0)

# print(result)
# print(result2)
dataset = {
    "Date": None,
    "Time": None,
    "W/L": None,
    "Class": None,
    "Killed_By": None,
    "Difficulty": None,
    "Time_Alive_": None,
    "TA_Pts": None,
    "Kills": None,
    "K_Pts": None,
    "Minion_Kills": None,
    "MK_Pts": None,
    "Deaths": None,
    "Damage_Dealt": None,
    "DD_Points": None,
    "Minion_Damage_Dealt": None,
    "MDD_Pts": None,
    "Most_Damage_Dealt": None,
    "Most_DD_Pts": None,
    "Damage_Taken": None,
    "Highest_Level": None,
    "HL_Pts": None,
    "Gold_Collected": None,
    "GC_Pts": None,
    "Items_Collected": None,
    "IC_Pts": None,
    "Stages_Completed": None,
    "SC_Pts": None,
    "Purchases": None,
    "Purch_Pts": None,
    "Total": None,
}


inputPath = input("Please paste your stats screenshot folder file path:\n")
