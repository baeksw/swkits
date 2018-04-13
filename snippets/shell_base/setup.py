from setuptools import setup

setup(
    name='swkit-shell-base',
    version='1.0',
    py_modules=['swkit'],
    include_package_data=True,
    install_requires=[
        'click',
        'click_shell',
        'click_repl',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        swkit=swkit.swkit:cli
    ''',
)
