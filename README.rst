.. image:: https://img.shields.io/pypi/v/skeleton.svg
   :target: https://pypi.org/project/skeleton

.. image:: https://img.shields.io/pypi/pyversions/skeleton.svg

.. image:: https://img.shields.io/pypi/dm/skeleton.svg

.. image:: https://img.shields.io/travis/jaraco/skeleton/master.svg
   :target: http://travis-ci.org/jaraco/skeleton

A FileLock class that implements a context manager with timeouts on top of
`zc.lockfile`, an excellent, cross-platorm implementation of file locking.

License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Usage
=====

Example usage::

    import yg.lockfile
    try:
    	with yg.lockfile.FileLock('/tmp/lockfile', timeout=900):
    		protected_operation()
    except yg.lockfile.FileLockTimeout:
    	handle_unable_to_lock()

