import numpy as np
import pandas as pd
import cv2
import os
from glob import glob

class CreateDataset():

    def __init__(self):
        self.height = 64
        self.width = 64
        self.dataframe = pd.DataFrame()
        self.Animatronic_Dict = {
            0: "Freddy",
            1: "Chica",
            2: "Bonnie",
            3: "Foxy",
            4: "Golden_Freddy",
            5: "Phone_Guy",
            #FNAF 2
            6: "Toy_Freddy",
            7: "Toy_Chica",
            8: "Toy_Bonnie",
            9: "Mangle",
            10: "Marionette",
            11: "BB",
            12: "JJ",
            13: "Withered_Chica",
            14: "Withered_Bonnie",
            #FNAF 3
            15: "Nightmare_Freddy",
            16: "Nightmare_Chica",
            17: "Nightmare_Bonnie",
            18: "Nightmare_Mangle",
            19: "Nightmare_Marionette",
            20: "Nightmare_BB",
            21: "Nightmare_Fredbear",
            22: "Phantom_Freddy",
            23: "Phantom_Mangle",
            24: "Phantom_BB",
            25: "Springtrap",
            26: "Plushtrap",
            #FNAF World
            27: "Old_Man_Consequences",
            28: "Dee_Dee",
            #FNAF: Sister Location
            29: "Funtime_Foxy",
            30: "Baby",
            31: "Ballora",
            32: "Minireena",
            33: "Bonnet",
            34: "Lolbit",
            35: "Ennard",
            #FNAF: Pizzeria Simulator
            36: "Rockstar_Freddy",
            37: "Rockstar_Chica",
            38: "Rockstar_Bonnie",
            39: "Happy_Frog",
            40: "Mr_Hippo",
            41: "Pig_Patch",
            42: "Nedd_Bear",
            43: "Orville_Elephant",
            44: "Helpy",
            45: "Lefty",
            46: "El_Chip",
            47: "Trash_and_the_Gang",
            48: "Molten_Freddy",
            49: "Funtime_Chica",
            50: "Shadow_Bonnie",
            51: "Scrap_Baby",
            52: "Fredbear",
            53: "William_Afton"
        }

    def create_Dataset(self):
        for name in os.listdir(""):
            print(f"Animatronic Image Name: {name}")

            for image_name in glob(f"AnimatronicsImages/{name}/*.jpg"):
                try:
                    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
                    image = cv2.resize(image, (self.height, self.width))
                    image = image.flatten()
                    image = np.append(image, self.Animatronic_Dict[name])
                    image_frame = pd.DataFrame(image, columns=[self.dataframe.shape[1]])
                    self.dataframe = pd.concat([self.dataframe, image_frame], axis=1)
                except:
                    pass
            
        if len(self.dataframe) != 0:
            self.dataframe = self.dataframe.T

    def create_CSV(self):
        self.dataframe.to_csv("AnimatronicsDataset.csv")


if __name__ == "__main__":
    dataset = CreateDataset()
    dataset.create_Dataset()
    dataset.create_CSV