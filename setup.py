from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name = "periodogram",
    version = "0.1",
    packages = find_packages(),

    install_requires = ['numpy>=1.8.1', 'matplotlib>=1.3.1', 'markdown'],

    entry_points = {
        'console_scripts': [
            'periodogram=periodogram.periodogram:__run',
            'periodogram-test=periodogram.test:__run'
        ]
    },

    author = "Roman Thiele",
    author_email = "r.thiele@tum.de",
    description = "A simple periodogram library",
    long_description = readme(),
    license = "MIT",
    keywords = "periodogram FFT DFT",
    url = "",

    include_package_data = True
)
