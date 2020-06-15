from matrix import Matrix

if __name__ == "__main__":
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
    m3 = Matrix((3, 3))

    print(m1.data)
    print(m2.data)
    print(m3.data)
    print(m1.shape)
    print(m2.shape)
    print(m3.shape)

    m4 = m1 + m1
    print(m4.data)

    m5 = m1 * 5
    print(m5.data)
