2.3
===

#5: Prefer `tempora <https://pypi.org/project/tempora>`_ to
jaraco.timing.

#4: Consolidate acquire, release, and is_locked behavior into LockBase.
Atomically remove lock attribute during release. Use jaraco.functools
1.16 for the retry logic.

Update package skeleton.

2.2.2
=====

Correct badges in README.

2.2.1
=====

#2: Suppress errors in the rare condition where the lockfile has
disappeared between the release of the lock and the deletion of
the file.

2.2
===

#3: Moved project to Github.

2.1
===

Re-use Stopwatch class from jaraco.timing.

2.0
===

Dropped support for Python 2.6.
