import zipfile
import json
import re
import time
import os

import pandas as pd
import pytesseract
from PIL import Image
from langdetect import detect
from textblob import TextBlob
a= time.time()
# from language_detector import detect_lang
def extractpng(file_path, filename, file_number):
    with open(f"{file_path}\{filename}_{str(file_number)}.png", 'wb') as outfile:
        file_name = f"{file_path}\{filename}.{str(file_number).zfill(3)}"
        try:
            with open(file_name, 'rb') as infile:
                outfile.write(infile.read())
        except FileNotFoundError:
            pass
def unzip_folder(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
def find_strings_with_pattern(strings):
    pattern = r"\.00"  # Pattern to search for (escaped dot followed by "003")
    matches = [string for string in strings if re.search(pattern, string)]
    return matches
def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"
def detect_language_TextBlob(text):
    try:
        blob = TextBlob(text)
        return blob.detect_language()
    except:
        return "Unknown"

a=[]
extract_path = 'D:\Qiagen\Bristol\ocrinput\ocrinput'
file_list = os.listdir(extract_path)
text_extract={}
for file_name in file_list:
    a.append(file_name)
    try:
        if os.path.isfile(os.path.join(extract_path, file_name)):
            unzip_folder(os.path.join(extract_path, file_name), extract_path)
            matching_strings = find_strings_with_pattern(os.listdir(os.path.join(extract_path, file_name[:-4])))
            text_extract[matching_strings[0][:-4]] = {}
            for i in range(len(matching_strings)):
                extractpng(os.path.join(extract_path, file_name)[:-4], file_name[:-4],i+1)
                text_extract[matching_strings[0][:-4]][str(i + 1)] = {}
                for f in [
                    os.path.join(os.path.join(extract_path, file_name)[:-4], matching_strings[0][:-4]) + "_" + str(
                            i + 1) + ".png"]:
                    with Image.open(f) as image:
                        tesseract_output = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
                        text = pytesseract.image_to_string(image, config='--psm 6')
                        image_content = detect_language(text)
                        text_extract[matching_strings[0][:-4]][str(i+1)]["text"] = text
                        text_extract[matching_strings[0][:-4]][str(i+1)]["language"] = image_content
                        text_extract[matching_strings[0][:-4]][str(i+1)]["length"] = len(text)
                        image_content = detect_language(text)
                        temp = process_document(extract_path + "\\"+ file_name[:-4] + "\\" + matching_strings[0][:-4] + "_" + str(
                            i + 1) + ".png")
                        # print(f"documnet type of {file} : {temp}")
                        image_content= "ww"
                        print(temp)
                        os.rename(os.path.join(os.path.join(extract_path, file_name)[:-4],
                                               matching_strings[0][:-4]) + "_" + str(i + 1) + ".png",
                                  os.path.join(os.path.join(extract_path, file_name)[:-4],
                                               matching_strings[0][:-4]) + "_" + str(i + 1) +  "_"  + temp['label'] + ".png")
    except:
        pass

b = time.time()
print(b-a)
