from setuptools import setup

setup(
    name='reddit_cli',
    description='A CLI to browse Reddit.',
    version='0.1',
    url='http://github.com/roshancvp/reddit_cli',
    author='Roshan Prabhakar',
    author_email='roshancvp@gmail.com',
    license='MIT',
    install_requires=[
    'click',
    'termcolor',
    'requests',
    ],
    entry_points='''
        [console_scripts]
        reddit_cli=reddit_cli:cli
    ''',
)
