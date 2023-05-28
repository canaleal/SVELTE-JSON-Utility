from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]


setup(
    name='traffic_processing',
    version='0.1',
    description='Traffic Processing Package',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Alex C',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
