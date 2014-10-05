===================
  Getting Started
===================

Installing pyRobotics
---------------------------------------

In order to use pyRobotics (or any other package) you need to have a copy of the package
in any of the folders included in the python path. You can do this in two ways: installing from a source 
distribution file from the ``dist`` folder in the source repository or from `pypi <https://pypi.python.org/pypi/pyRobotics>`_,
or manually copying the source package into a location in the PYTHONPATH. You can download the package from
`here <http://github.com/BioRoboticsUNAM/pyRobotics>`_.

.. note::

  Note that the git repository includes some examples, as well as the library, the package is the FOLDER named pyRobotics
  within the repository.

*To install from a distribution file*

Simply extract the contents of the file with the command ``tar -xzvf pyRobotics-<version>.tar.gz``
and then run ``python setup.py install`` (You might need superuser permissions).

*To copy the source package in a location in the PYTHON_PATH*

To know which folders are in the ``PYTHON_PATH``, open an interactive console and type:

  >>> import sys
  >>> sys.path

Alternatively, you can modify your python configuration to include in the ``PYTHON_PATH`` whichever folder ``pyRobotics``
is located in.

.. _creating_a_command_handler:

Creating a Command Handler
-----------------------------
.. currentmodule:: pyrobotics.messages

A command handler is a function that receives a :class:`Command` object and returns a
:class:`Response` object.

The Response object should be created by the class function :func:`Response.FromCommandObject`. This is important
because every command has an internal id to keep track of commands and responses, and this functions creates the approppriate
response.

Here you can see an example of a command handler::

  def myCommandHandler(commandObj):
    params = parseCommandParams(commandObj.params)

    if executeCommand(params):
      return Response.FromCommandObject(commandObj, True, "answer successful")

    return Response.FromCommandObject(commandObj, False, "answer UNsuccessful")

Notice that the last parameter is meant to be the actual return value of the command, in case the command should answer
something, such as a list of recognized objects, the name of a recognized face, etc.
If the command is not supposed to answer anything but whether it was successful or not, it doesn't matter what this
parameter has, it can be an empty string or they keyword ``None``, in which case the response will be sent with the original
parameters.

.. _creating_a_subscription_handler:

Creating a Subscription Handler
---------------------------------

A subscription hanlder is a function that will execute whenever a notification of an updated shared variable is received.
(Whenever somebody writes to it). It receives a :class:`SharedVar <pyrobotics.shared_variables.SharedVar>` object and should not return anything.

Since the function receives the SharedVar object, it has the information of what type of shared var it is, and its data, so
there could be one subscription handler for more than one shared variable (or all) and the handler should then decide
what to do with them.

Here's an example of a simple subscription handler that prints the info of the shared variable::

  def mySubscriptionHandler(sv):
    print '----------------------------'
    print 'Shared Variable updated:'
    print sv.varName
    print sv.svType
    if sv.size >= 0:
      print sv.size
    print sv.data


.. _creating_a_simple_module:

Creating a Simple Module
---------------------------

This is an example included with the :ref:`source code <source_code>`::

  import time
  from pyrobotics import BB
  from pyrobotics.parallel_senders import ParallelSender
  from pyrobotics.messages import Command, Response

  # These command handler functions could (and probably should) be defined in another module
  # as to keep the main program file simple and clean.
  def testFunction(c):
    print "testFunction called..."
    print 'Params: ' + c.params
    return Response.FromCommandObject(c, True, 'Command response')

  fmap = {
       'tst_testfunction' : testFunction
  }


  def main():
    BB.Initialize(2000, fmap)
    BB.Start()
    BB.SetReady(True)
    
    print 'Sending command say...'
    print BB.SendAndWait(Command('spg_say', 'This is a test.'), 5000, 3)
    
    print 'Sending Async command...'
    ps = ParallelSender(Command('othertst_slowfunction', 'This is another test.'), 5000, 3)
    
    while ps.sending:
      print 'sending...'
      time.sleep(0.3)
  
    print 'Response received...'
    print ps.response
    
    BB.Wait()

  if __name__ == "__main__":
    main()
