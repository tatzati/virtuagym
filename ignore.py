class Parent:
    variable = None

    def run(self):
        print(self.variable)


class Child(Parent):
    variable = 'testing'


child = Child()
child.run()
child.run()
child.run()
