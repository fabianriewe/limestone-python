import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    requires = req.readlines()
    requires = list(map(lambda x: x.strip(), requires))

setuptools.setup(
    name="limestone-finance",
    version="0.0.1",
    author="Fabian Riewe",
    author_email="fabian@kyve.network",
    description="A python wrapper for limestone.finance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fabianriewe/limestone-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requires
)
