class vehicle:
    color=" "
    name=" "
    tyres=" "
    proof="ragistration"
    def f1(self):
      print(f"the car has valid {self.proof}.")
class car(vehicle):
  tyres=4
  name="hector"
  fueltype="diesel"
  color="Blue"
  def f1(self):
    super().f1()
    print(f"The car name is {self.name}.It has {self.tyres} tyres.Its fuel type is {self.fueltype} and its color is {self.color}.")
c=car()
c.f1()