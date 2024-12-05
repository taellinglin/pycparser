from setuptools import setup, find_packages

setup(
    name="pycparser",  # Use the appropriate project name
    version="2.21",  # Replace with the correct version if available
    description="A C parser and AST generator written in pure Python",
    long_description = "A C parser and AST generator written in pure Python",
    long_description_content_type="text/markdown",
    author="Eli Bendersky",
    author_email="eliben@gmail.com",
    url="https://github.com/taellinglin/pycparser",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],  # Specify dependencies here
)
