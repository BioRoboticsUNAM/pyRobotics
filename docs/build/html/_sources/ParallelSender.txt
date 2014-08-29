======================================
  Parallel (or asynchronous) Sender
======================================

.. currentmodule:: pyRobotics.ParallelSenders

.. autoclass:: ParallelSender
  :members:

----------
Example
----------

.. highlight:: python
  :linenothreshold: 5

::

  from pyRobotics import BB
  from pyRobotics.ParallelSenders import ParallelSender as PS
  from otherModule import fastCommand, slowCommand

  function_map = {
                  'fast_command': fastCommand,
                  'slow_command': slowCommand

  def initialize():
    global function_map
    BB.Initialize(2000, function_map)
    BB.Start()
    BB.SetReady()

  def main():
    initialize()

    p = PS(Command('command_name', 'command_params'), 3000)

    while p.sending:
      #do something
      print 'sending message...'

    if not p.response:
      print 'Sending failed, probably timed out.'
      return

    if p.response.result:
      print 'command was successful!'
    else:
      print 'command execution was UNsuccessful!'}

    BB.Wait()

  if __name__ == '__main__':
    main()

