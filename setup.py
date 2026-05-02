from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-SMART-MANUFACTURING-MACHINES-EFFICIENCY-PREDICTION",
    version="0.1",
    author="SIRIDACH JAROENSIRI",
    packages=find_packages(),
    install_requires = requirements,
)