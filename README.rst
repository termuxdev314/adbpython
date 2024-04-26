adbpython
=========

Python ADB Modul

Install
-------

.. code-block:: bash

   pip install adbpython

use
---

.. code-block:: python

   import adbpython as adb
   
  device = adb.connection
  device.connect(ip, port)
  shell = adb.shell
  event = shell.keyevent
  