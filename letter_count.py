class Class:
  def __init__(self, x):
    sefl.x = x
  def function(self):
    y = self.x.split()
    count = 0
    dict = {}
    for word in y:
      if word.isalpha():
        count = y.count(word)
        dict[word] = count
    return dict
