# !/usr/bin/python

#   The FiltSort function need an input: the path to a folder,
#   and then it will generate an output.txt file that includes
#   the "index, file name, address, maintag, subtag, subtag2"
#   of every file in that folder.
#   It can also return the output file as a list.

import os

def setLabel(path):
    indexs = []
    index = 0
    for p in path:
        if p == "/":
            indexs.append(index)
        index += 1
    main_tag, sub_tag, sub_tag2, file = "None", "None", "None", "None"

    if len(indexs) == 1:
        file = path[(indexs[0] + 1):]
    if len(indexs) == 2:
        main_tag = path[(indexs[0] + 1) : indexs[1]]
        file = path[(indexs[1] + 1):]
    if len(indexs) == 3:
        main_tag = path[(indexs[0] + 1) : indexs[1]]
        sub_tag = path[(indexs[1] + 1) : indexs[2]]
        file = path[(indexs[2] + 1):]
    if len(indexs) == 4:
        main_tag = path[(indexs[0] + 1) : indexs[1]]
        sub_tag = path[(indexs[1] + 1) : indexs[2]]
        sub_tag2 = path[(indexs[2] + 1) : indexs[3]]
        file = path[(indexs[3] + 1):]

    return [file, path, main_tag, sub_tag, sub_tag2]

def str2Label(line):
    return line.split(", ")

def label2Str(labels):
    output = ', '.join(label for label in labels)
    return output

def isFile(file):
    return "." in file

# check whether the file is the hidden file, and whether the dictionary contains no file.
def isValidLabel(labels):
    for label in labels:
        if label[0] == ".":
            return False
    return isFile(labels[0])

def output2List():
    output = open("output.txt", "r")
    elements = output.readlines()
    output_list = []
    for element in elements:
        output_list.append(str2Label(element))
    return output_list

def FileSort(path):
    if os.path.exists("output.txt"):

        output = open("output.txt", "r")
        output_update = open("output_update.txt","w")

        elements = output.readlines()
        names =[]

        for element in elements:
            names.append(str2Label(element)[2])
            output_update.write(element)

        output.close()
        index = len(names)

        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:

                root_length = len(path)
                file_name = str(os.path.join(root, name))[(root_length):]
                labels = setLabel(file_name)

                if isValidLabel(labels) and labels[1] not in names:

                    result = label2Str(labels)
                    output_update.write(str(index) + ", " + result + "\n")
                    index += 1

        os.rename("output_update.txt", "output.txt")
        output_update.close()

    else:

        output = open("output.txt","w")
        index = 0

        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:

                root_length = len(path)
                file_name = str(os.path.join(root, name))[(root_length):]
                labels = setLabel(file_name)

                if isValidLabel(labels):

                    result = label2Str(labels)
                    output.write(str(index) + ", " + result + "\n")
                    index += 1

        output.close()
    return output2List()
