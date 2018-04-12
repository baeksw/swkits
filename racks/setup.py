
try:
    from setuptools import setup
except:
    from  distutils.core import setup


dependencies = [ 'docopt', 'termcolor' ]

setup(
    name='racks',
    version='0.0.1',
    description='racks on rack for stack graphs',
    url='http://www.github.com/swbaek/racks',
    author='SeungWoo.BAEK',
    author_email='dohaskell7@gmail.com',
    install_requires=dependencies,
    packages=['racks'],
    entry_points={
        'console_scripts': [
            'racks=racks.main:start'
        ],
    },
    classifiers=(
        'Development Status :: 1 - Beta',
        'Intended Audience :: developers',
        'Natural Language :: English or Korean',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python 3.x',
    ),
)
