from setuptools import setup, find_packages

setup(
    name='my_diff_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_diff=my_diff_tool.ccdiff:main',
        ],
    },
    author='Rajeev Kumar',
    author_email='rajeevnita29@gmail.com',
    description='A custom diff tool in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rajeevnita1993/my_diff_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)