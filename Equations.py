class Equations:
    def __init__(self, eqn, age, studentClass):
        self.name = name
        self.age= age
        self.studentClass = studentClass
        
    def __str__(self):
        output = '-' * 20 + '\n'
        output += '{:<10}'.format('Name=')
        output += '{:>10}\n'.format(self.name)
        output += '{:<10}'.format('Age=')
        output += '{:>10}\n'.format(self.age)
        output += '{:<10}'.format('Class=')
        output += '{:>10}\n'.format(self.studentClass)
        return output