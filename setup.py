from setuptools import setup, find_packages

requirements = [
    'opencv-python',
    'opencv-contrib-python',
    'scikit-image',
    'scipy',
    'numpy',
    'matplotlib',
    'imutils',
]


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="kn_iris",
    version="0.1",
    description="A Python package to iris based activities.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Gate6",
    author_email="2017170@iiitdmj.ac.in",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3",

    ],
    # packages=find_packages(),
    packages=["kn_iris"],
    include_package_data=True,
    install_requires=requirements,
    # install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'G6_iris_recognition=kn_iris.main:main',
        ]
    },
)
