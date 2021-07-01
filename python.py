class Class:
  def __init__(self):
    
  def function(self, x):
    y = self.x.split()
    count = 0
    dict = {}
    for word in y:
      if word.isalpha():
        count = y.count(word)
        dict[word] = count
    return dict
