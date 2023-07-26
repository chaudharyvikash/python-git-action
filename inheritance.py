class Bigfix:
    def __init__(self, project):
        self.project= project

    
    def showProject(self):
        print(f"The name of Project is {self.project}")



class Patch(Bigfix):
    def __init__(self, project):
        self.project= project

    def currentProject(self):
        print(f"The name of Current Project is {self.project}")

p=Bigfix('kev')
p.showProject()

p2=Patch('patch')
p2.currentProject()
p2.showProject()