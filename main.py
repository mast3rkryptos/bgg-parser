import csv
import re

with open('collection.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print reader.fieldnames
    for row in reader:
        print(str(row['objectname']).decode('utf8'), row['own'])

    # Regular Expression Pattern: Sleeves:[count][type][count][type]...
    s = "Sleeves:1234SA11223344MA1432(70x70)666(12x34)"
    p = re.compile("Sleeves:([\w\(\)]+)")
    m = p.match(s)
    print m.group(1)
    p = re.compile("(\d+)(\(\d+x\d+\)|[A-Za-z]+)")
    groups = p.findall(m.group(1))
    print groups

    # (Official Size, width(mm), height(mm), NSKN Name)
    dictSleeves = {
        "S":   ("Standard Board Game/CCG", 63, 89, "Percival"),
        "SA":  ("Standard American", 57, 89, "Gawain"),
        "MA":  ("Mini American", 41, 63, "Galahad"),
        "SE":  ("Standard European", 59, 92, "Tristan"),
        "ME":  ("Mini European", 45, 68, "Arthur"),
        "SSq": ("Small Square", 51, 51, "Palamedes"),
        "Sq":  ("Square", 70, 70, "Kai"),
        "LSq": ("Large Square", 80, 80, "Owain"),
        "ASp": ("American Special", 54, 86, "Ragnar"),
        "L":   ("Large", 65, 100, "Lancelot"),
        "T":   ("Tarot", 70, 120, "Bors"),
        "M":   ("Medium", 50, 75, "Lohengrin"),
        "MP":  ("Medium Plus", 54, 80, "Bedivere"),
        "SpA": ("Specialist A", 70, 110, "Lamorac"),
        "SpB": ("Specialist B", 80, 120, "Gaheris"),
        "XL":  ("XL", 89, 146, "Morholt"),
        "QT":  ("Queen Tarot", 61, 112, "Gudrun"),
        "ESp": ("Epic Specialist", 88, 126, "Pellinore"),
        "XLP": ("XL Plus", 101.5, 153, "Morgana"),
        "SpC": ("Specialist C", 103, 128, "Ragnelle"),
        "XXL": ("XXL", 101.5, 203, "Mordred")
    }

    for group in groups:
        if group[1] in dictSleeves.keys():
            print group[0], dictSleeves[group[1]][0]
        else:
            foundKey = ""
            for k in dictSleeves:
                p = re.compile("\((\d+)x(\d+)\)")
                m = p.match(group[1])
                if int(m.group(1)) == dictSleeves[k][1] and int(m.group(2)) == dictSleeves[k][2]:
                    foundKey = k
            if foundKey:
                print group[0], dictSleeves[foundKey][0]
            else:
                print group[0], group[1]
