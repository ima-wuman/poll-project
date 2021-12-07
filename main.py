print ('''vote for one of these:
1. Machine Learning
2. Blockchain
3. Advanced Web development
4. UI design
''')

def vote(x):
  Machine_Learning = 0
  Blockchain = 0
  Advanced_Web_development = 0
  UI_design = 0
  if x == '1':
    Machine_Learning = Machine_Learning + 1
    print ('you voted for Machine Learning')
  elif x == '2':
    Blockchain = Blockchain + 1
    print ('you voted for Blockchain')
  elif x == '3':
    Advanced_Web_development = Advanced_Web_development + 1
    print ('you voted for Advanced Web development')
  elif x == '4': 
    UI_design = UI_design + 1
    print ('you voted for UI design')
  else:
    print('choose the responding number')
    vote(input())
    return 
  print ('''
votes:''')
  print ('Machine Learning ' + str(Machine_Learning))
  print ('Blockchain ' + str(Blockchain))
  print ('Advanced Web development ' + str(Advanced_Web_development))
  print ('UI design ' + str(UI_design))

  

vote(input())
