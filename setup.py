from distutils.core import setup

setup(
    name='android-missingdrawables',
    version='1.0',
    description='Easily find out for which density buckets your drawables are missing.',
    license='MIT',
    author='Hannes Struss',
    author_email='x@hannesstruss.de',
    url='https://github.com/hannesstruss/android-missingdrawables',
    py_modules=['missingdrawables'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'missingdrawables=missingdrawables:main',
        ],
    },
)
