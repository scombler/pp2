class myclass():
  def __len__(self):  # an object that is made from a class with a __len__ function will returns 0 or False:
    return 0

myobj = myclass()
print(bool(myobj))