from setuptools import find_packages, setup
setup(
    name='mypyconf',
    packages=find_packages(include=['mypyconf']),
    version='0.1.0',
    description='Python Configuration Reader',
    author='09hirenpatel',
    license='MIT',
    install_requires=[
        'pyyaml',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)