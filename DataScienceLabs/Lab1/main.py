import requests

# Returns a dictionary from a 3D object
def getDicFromObj():
    pointcloud = {}

    obj = requests.get("https://raw.githubusercontent.com/porterjenkins/cs180-intro-data-science/master/data/plane.obj")
    data = obj.text.splitlines()

    vertices = []
    faces = []
    for row in data:
        tempRow = row.split()
        if tempRow[0] == 'v':  # vertices
            floatList = [float(i) for i in tempRow[1:]]
            vertices.append(floatList)
        elif tempRow[0] == 'f':  # faces
            if '/' in row:
                intList = []
                for i in range(1, len(tempRow)):
                    item = tempRow[i]
                    slashIndex = item.find('/')
                    newItem = item[:slashIndex]
                    intList.append(int(newItem))
            else:
                intList = [int(i) for i in tempRow[1:]]
            faces.append(intList)

    pointcloud["vertices"] = vertices
    pointcloud["faces"] = faces

    return pointcloud


pointcloud = getDicFromObj()