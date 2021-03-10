from setuptools import setup

setup(name='fgazat_replacer',
      python_requires='>3.6',
      version='1.0.1',
      description='Replaces commas to dots',
      entry_points={
          'console_scripts':
              ['replacer = main:main'],
      },
      zip_safe=False)
