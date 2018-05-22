.. image:: https://img.shields.io/pypi/v/yg.lockfile.svg
:target: https://pypi.org/project/yg.lockfile

.. image:: https://img.shields.io/pypi/pyversions/yg.lockfile.svg

.. image:: https://img.shields.io/travis/yougov/yg.lockfile/master.svg
   :target: https://travis-ci.org/yougov/yg.lockfile

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/skeleton/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/skeleton/branch/master

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest


A FileLock class that implements a context manager with timeouts on top of
`zc.lockfile`, an excellent, cross-platorm implementation of file locking.

Usage
=====

Example usage::

    import yg.lockfile
    try:
    	with yg.lockfile.FileLock('/tmp/lockfile', timeout=900):
    		protected_operation()
    except yg.lockfile.FileLockTimeout:
    	handle_unable_to_lock()

