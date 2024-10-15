from setuptools import setup, find_packages

setup(
    name='historical_earnings',  # The name of your package on PyPI
    version='0.1',
    description='A package to query historical earnings report dates for stock tickers',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/historical_earnings_package',  # Link to your GitHub repo
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'historical_earnings': ['data/aggregated_earnings_data_webscraped.csv'],  # Update package name here
    },
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
