import json
import glob

src = "sampleJson/"
result = []
files = glob.glob('sampleJson/*', recursive= True)

for single_file in files:
    with open(single_file, 'r+') as infile:
        result.append(json.load(infile))

for dic in result:
    #print(dic)
    for object in dic['objects']:
        # print(object['classTitle'])
        if object['classTitle'] == 'Vehicle':
            object['classTitle'] = 'car'
            # print(object['classTitle'])
        elif object['classTitle'] == 'License Plate':
            object['classTitle'] = 'number'
            # print(object['classTitle'])




with open('final.json', 'w') as outputf:
    json.dump(result,outputf, indent= 2)


