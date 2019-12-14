import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neuroevn",
    version="0.0.1",
    description="Package for applying NeuroEvolution strategies",
    url="https://github.com/neuropark/NeuroEVN",
    packages=setuptools.find_packages(),
    python_requires='>= 3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
)
