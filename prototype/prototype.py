class A(object): 
  def clone(self, **attr):
    obj = deepcopy(self)
    obj.__dict__.update(attr)
    return obj

if __name__ == "__main__":
  a = A()
  
  a.q = 'q'
  b = a.clone(a=1, b=2, c=3)  
  
  print b.q, b.a, b.b, b.c
  b.d = '4'
  c = b.clone(e='5')
  print c.q, c.a, c.b, c.c, c.d, c.e
 
