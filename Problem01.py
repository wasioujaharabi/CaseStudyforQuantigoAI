import json
src = 'pos_0.png.json'
with open('./sampleJson/%s' %src)as f:
    data = json.load(f)

vehicle_dic = {
    "dataset_name": src,
    "image_link": "",
    "annotation_type": "image",
    "annotation_objects": {
        "vehicle": {
            "presence": 0,
            "bbox": []
        },
        "license_plate": {
            "presence": 0,
            "bbox": []
        }
    },
    "annotation_attributes": {
        "vehicle": {
            "Type": None,
            "Pose": None,
            "Model": None,
            "Make": None,
            "Color": None
        },
        "license_plate": {
            'Difficulty Score': None,
            'Value': None,
            'Occlusion': None
        }
    }
}


for object in data['objects']:
    if 'classTitle' in object:
        if object['classTitle']== 'Vehicle':
            vehicle_dic["annotation_objects"]["vehicle"]["presence"]+=1
            vehicle_dic["annotation_objects"]["vehicle"]["bbox"] = object["points"]["exterior"][0]+object["points"]["exterior"][1]
            for tag in object['tags']:
                vehicle_dic["annotation_attributes"]["vehicle"][tag['name']] = tag['value']

        elif object['classTitle']== 'License Plate':
            vehicle_dic["annotation_objects"]["license_plate"]["presence"] += 1

            vehicle_dic["annotation_objects"]["license_plate"]["bbox"] = object["points"]["exterior"][0] + \
                                                                   object["points"]["exterior"][1]

            for tag in object['tags']:
                vehicle_dic["annotation_attributes"]["license_plate"][tag['name']] = tag['value']

            vehicle_dic["annotation_attributes"]["license_plate"]['Occlusion'] = 0


filename='formatted_%s' %src

with open(filename, 'w') as outputf:
    json.dump([vehicle_dic],outputf, indent= 2)
