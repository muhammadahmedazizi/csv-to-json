# import packages for csv and json

import csv, json

# read csv file and add to data


data = {}
with open('sample-blog-data-with-header.csv', 'r', encoding='utf-8-sig') as csvFile:
    csvReader = csv.DictReader(csvFile)
    #print (csvReader)

    for csvRow in csvReader:
        key = csvRow['title']
        print (key)
        data[key] = csvRow
        print (data)


# create new json file and write data on it
with open('output.json', 'w', encoding='utf-8') as jsonFile:
    # make it more readeable and pretty
    jsonFile.write(json.dumps(data, indent=4))

