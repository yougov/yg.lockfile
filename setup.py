#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

needs_wheel = {'release', 'bdist_wheel', 'dists'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

name = 'yg.lockfile'
description = 'Lockfile object with timeouts and context manager'

py33_markers = [
	'python_version=="{ver}"'.format(**locals())
	for ver in ('3.3', '3.2', '2.7')
]
py33 = ':' + ' or '.join(py33_markers)

setup_params = dict(
	name=name,
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/yougov/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=[
		'zc.lockfile',
		'jaraco.timing',
	],
	extras_require={
		py33: [
			"contextlib2>=0.5",
		],
	},
	setup_requires=[
		'setuptools_scm>=1.15.0',
	] + wheel,
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points={
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
