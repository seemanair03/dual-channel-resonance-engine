from setuptools import setup, find_packages

setup(
    name="resonance",
    version="0.1.0",
    author="Seema",
    description="A poetic presence layer for courage-aware systems.",
    long_description=open("resonance/README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["resonance", "resonance.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.7",
)