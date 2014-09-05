'''
@author: arcra
'''

import time
from pyRobotics import BB
from pyRobotics.Messages import Command, Response

def slowFunction(c):
    print "slow function called..."
    time.sleep(3)
    r = BB.SendAndWait(Command('tst_testfunction', "This is another test."), 3000)
    success = r and r.successful
    return Response.FromCommandObject(c, success, 'Slow Command response')

fmap = {
        'othertst_slowfunction' : (slowFunction, True)
        }



def main():
    BB.Initialize(2001, fmap)
    BB.Start()
    BB.SetReady(True)
    
    print 'Waiting for commands...'
    BB.Wait()

if __name__ == "__main__":
    
    main()
