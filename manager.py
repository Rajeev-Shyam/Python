from person import Person

class Manager(Person):
    def __init__(self, name, job, salary,project):
        super().__init__(name, job, salary)
        self._project=project
    
    def getproject(self):
        return self._project
    def setproject(self,project):
        self._project=project
    project=property(getproject,setproject)

    def __str__(self):
        return ("%s with the job %s" % (super().__str__,self._project))