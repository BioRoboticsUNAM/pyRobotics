'''
@author: arcra
'''

from pyRobotics import BB

def printingFunc(svar):
    
    print 'Data published: ' + str(svar.data)

def main():
    BB.Initialize(2003)
    
    BB.Start()
    
    BB.SubscribeToSharedVar('test_string', printingFunc)
    
    print 'Waiting for shared variable updates...'
    
    BB.Wait()

if __name__ == '__main__':
    main()

