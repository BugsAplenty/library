import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="library-neiman", # Replace with your own username
    version="0.0.1",
    author="Michael Perfetto",
    author_email="michaeln.perfetto@gmail.com",
    description="A python test exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://13.92.98.39.nip.io/rla/algo/TRAIN/library-neiman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)