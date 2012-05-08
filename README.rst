yg.lockfile
===========

A LockFile class that implements a context manager with timeouts on top of
`zc.lockfile`, an excellent, cross-platorm implementation of file locking.

Usage
-----

Example usage::

    import yg.lockfile
    try:
    	with yg.lockfile.LockFile('/tmp/lockfile', timeout=900):
    		protected_operation()
    except yg.lockfile.LockFileTimeout:
    	handle_unable_to_lock()
