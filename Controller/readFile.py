import pickle


def updateFile(filePath):
    # initializing data to be stored in db
    Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
             'age': 21, 'pay': 40000}
    Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
               'age': 50, 'pay': 50000}

    # database
    db = [Omkar, Jagdish]

    # Its important to use binary mode
    dbfile = open(f'{filePath}', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()


def readFile(filePath):
    # for reading also binary mode is important
    dbfile = open(f'{filePath}', 'rb')
    db = pickle.load(dbfile)
    # Print content file:
    print(db)
    dbfile.close()
    return db
