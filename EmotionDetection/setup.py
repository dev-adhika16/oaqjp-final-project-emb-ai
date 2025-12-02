"""Setup configuration for EmotionDetection package."""

from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="A simple emotion detection package using IBM Watson NLP service",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/dev-adhika16/oaqjp-final-project-emb-ai",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)
