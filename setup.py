from setuptools import setup, find_packages


requires = [
    "argparse",
    "pyramid",
]

points = {
    "console_scripts":[
        "psetup=rebecca.setupapp.commands:main",
    ]
}

setup(
    name="rebecca.setupapp",
    namespace_packages=['rebecca'],
    install_requires=requires,
    packages=find_packages(),
    test_suite='rebecca.setupapp',
    entry_points=points,
)
