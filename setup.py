from distutils.core import setup

setup(
    name='android-missingdrawables',
    version='0.1',
    description='Easily find out for which density buckets your drawables are missing.',
    author='Hannes Struss',
    author_email='x@hannesstruss.de',
    url='https://github.com/hannesstruss/android-missingdrawables',
    py_modules=['missingdrawables'],
    entry_points={
        'console_scripts': [
            'missingdrawables=missingdrawables:main',
        ],
    },
)
