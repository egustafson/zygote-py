================
Title for Zygote
================

Prerequisites
=============

None. (yet)


Installation
============

Install locally using:

.. code::

    > python setup.py develop --user

The above command deploys the project in "Development Mode" using the
develop_ verb.  The project is deployed into the user's home directory
with the '--user' flag.

.. _develop:
https://setuptools.pypa.io/latest/setuptools.html#develop-deploy-the-project-source-in-development-mode

The files will be deployed into a tree under ``~/.local``.  Adding
``~/.local/bin`` to your path is sufficient to execute the local
copies, or run files from .local/bin using there full path.

Testing
=======

Unit tests, using `Python unittest`_ can be run using Python Nose_ (v1)

.. _Python unittest:  https://docs.python.org/3/library/unittest.html
.. _Nose: https://nose.readthedocs.org/en/latest/

.. code::
   
    > nosetests



.. ## End of document
