from setuptools import setup, find_packages

setup(
    name='morse-tunes',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'morse-tunes=main:main'
        ]
    },
    author="Muhammad Wisal",
    author_email="muhammadwisalkhanmv@example.com",
    description="A library to convert text to Morse code and play it as audio.",
    url="https://github.com/wisalkhanmv/morse-tunes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
