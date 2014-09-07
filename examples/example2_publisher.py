'''
@author: arcra
'''

from pyrobotics import BB
from pyrobotics.shared_variables import SharedVarTypes

def createVar():
    if BB.CreateSharedVar(SharedVarTypes.STRING, 'test_string'):
        print 'Var created'
    else:
        print 'Var NOT created'

def writeVar():
    print 'What would you like to write?'
    s = raw_input(':')
    if BB.WriteSharedVar(SharedVarTypes.STRING, 'test_string', s):
        print 'Written to var: ' + str(s)
    else:
        print 'Var NOT written'

def readVar():
    r = BB.ReadSharedVar('test_string')
    
    if r:
        print 'Var read: ' + str(r)
    else:
        print 'Var NOT read'

def main():
    
    BB.Initialize(2002)
    BB.Start()
    BB.SetReady(True)
    
    s = ''
    while s != '4':
        print '1. Create var'
        print '2. Write var'
        print '3. Read var'
        print '4. exit'
        
        s = raw_input(':')
    
        if s == '1':
            createVar()
        elif s == '2':
            writeVar()
        elif s == '3':
            readVar()
            
if __name__ == '__main__':
    main()
        
