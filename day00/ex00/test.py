from vector import Vector

if __name__ == "__main__":
    #__init__
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    v2 = Vector(3)
    v3 = Vector((10,15))
    #v4 = Vector("salut")
    #v5 = Vector()
    #print(v1.values)
    #print(v2.values)
    #print(v3.values)
    #print(v4.values)
    #print(v5.values)
    
    #__add__
    v6 = v1 - 4
    print(v6.values)
    v7 = v1 + v6.values
    #print(v7.values)
    v8 = v1 + v6
    #print(v8.values)
    v9 = v1 + v2
    #print(v9.values)
    v10 = v1 + "salut"
    #print(v10.values)

    #__radd__
    v11 = 4 + v1
    #print(v11.values)

    #__mul__
    v12 = v1 * 4
    v13 = v1 * v1.values
    v14 = v1 * v1
    print("%r %v12")
    print(v13)
    print(v14)
    v12

