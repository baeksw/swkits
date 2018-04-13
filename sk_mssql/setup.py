from setuptools import setup

setup(
    name='skmssql',
    version='0.0.1',
    py_modules=['sk_cmd'],
    include_package_data=True,
    install_requires=[
        'click',
        'click_shell',
        'click_repl',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        skmssql=sk_cmd.main:start
    ''',
)
