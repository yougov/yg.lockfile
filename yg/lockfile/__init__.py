#!/usr/bin/env python

"""
Cross-platform file lock context
"""

import os
import time
import functools

import zc.lockfile

class FileLockTimeout(Exception):
    pass

class FileLock(object):
    """
    A cross-platform locking file context.

    May be used in a with statement to provide system-level concurrency
    protection.

    This class relies on zc.lockfile for the underlying locking.

    This class is not threadsafe.
    """

    def __init__(self, lockfile, timeout=10, delay=.05):
        """
        Construct a FileLock. Specify the file to lock and optionally
        the maximum timeout and the delay between each attempt to lock.
        """
        self.lockfile = lockfile
        self.timeout = timeout
        self.delay = delay

    def acquire(self):
        """
        Attempt to acquire the lock every `delay` seconds until the
        lock is acquired or until `timeout` has expired.

        Raises FileLockTimeout if the timeout is exceeded.

        Errors opening the lock file (other than if it exists) are
        passed through.
        """
        start_time = time.time()
        attempt = functools.partial(zc.lockfile.LockFile, self.lockfile)
        while True:
            try:
                self.lock = attempt()
                break
            except zc.lockfile.LockError:
                timeout_expired = time.time()-start_time >= self.timeout
                if timeout_expired:
                    raise FileLockTimeout()
                time.sleep(self.delay)

    def is_locked(self):
        return hasattr(self, 'lock')

    def release(self):
        """
        Release the lock and delete the lockfile.
        """
        if self.is_locked():
            self.lock.close()
            del self.lock
            os.remove(self.lockfile)

    def __enter__(self):
        """
        Acquire the lock unless we already have it.
        """
        if not self.is_locked():
            self.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self.release()

    def __del__(self):
        """
        Release the lock on destruction.
        """
        self.release()
