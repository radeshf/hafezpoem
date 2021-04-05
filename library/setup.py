from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='hafezpoem',
    version='1.1.0',
    description="Random poem of hafez for restaurant factor and other staff",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='',
    author='Radesh Farokhmanesh',
    author_email='radesh.farokhmanesh@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='hafez fal poem factor restaurant',
    packages=find_packages(),
    install_requires=[''],
    include_package_data=True,
)