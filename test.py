def sumthemallup(**args):
    for i,v in args.items():
        print(i,v)

class U2UStudent:
    '''Represents a U2U student'''
    nrofstudents = 0

    def __init__(self,firstname: str, lastname:str) -> None:
        '''Provide the official firstname and last name as on the passport'''
        self._fname = firstname
        self._lname = lastname
        U2UStudent.nrofstudents +=1

    @property
    def FirstName(self):
        self._askedForName = True
        return self._fname
    
    @FirstName.deleter
    def FirstName(self):
        self._fname = "John"

u2uwebsite = "https://www.u2u.be"

sumthemallup(height=10,width=20)

