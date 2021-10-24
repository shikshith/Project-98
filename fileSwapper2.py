def dataSwapper ( ):
    print("Please Put Your First File Here")
    file1 = input()

    print("Please Put the Other FIle's name Here ")
    file2 = input()

    with open(file1,'r') as a:
        data_a=a.read()
    
    with open(file2,'r') as a:
        data_b=a.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2,'w') as a:
        a.write(data_b)

    
    dataSwapper()
    