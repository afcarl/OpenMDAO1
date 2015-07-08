
import os
import sys
from distutils.core import setup

setup(name='openmdao',
      version=1.0,
      description="OpenMDAO v1 framework infrastructure",
      long_description="""\
""",
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
      ],
      keywords='optimization multidisciplinary multi-disciplinary analysis',
      author='',
      author_email='',
      url='http://openmdao.org',
      license='Apache License, Version 2.0',
      packages=[
          'openmdao',
          'openmdao.core',
          'openmdao.core.test',
          'openmdao.util',
          'openmdao.test',
          'openmdao.units',
          'openmdao.components',
          'openmdao.drivers',
          'openmdao.doegenerators',
          'openmdao.surrogatemodels',
      ],
      install_requires=[
        'six', 'Sphinx', 'numpydoc', 'networkx', 'numpy'
      ],
      entry_points= """
        [console_scripts]
        wingproj=openmdao.devtools.wingproj:run_wing
      """
    )
