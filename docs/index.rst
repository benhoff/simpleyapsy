.. pluginmanager documentation master file, created by
   sphinx-quickstart on Tue Sep 29 00:01:54 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pluginmanager's documentation!
=======================================
pluginmanager is a `GPL3 Licensed <http://opensource.org/licenses/GPL-3.0>`_ plugin manager, written in Python.

**WARNING:** This library is under HEAVY development.

if you'd like to help, `fork on GitHub <https://github.com/benhoff/pluginmanager>`_!

::
    plugin_interface = pluginmanager.Interface()
    plugin_interface.set_plugin_directories('fancy/plugin/path')
    plugins = plugin_interface.collect_plugins()
