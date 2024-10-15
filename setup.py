from setuptools import setup, find_packages

setup(
    name='historical_earnings_package',
    version='0.1',
    description='A package to query historical earnings report dates for stock tickers',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,  # Include non-code files (like CSV)
    package_data={
        'historical_earnings_package': ['data/aggregated_earnings_data_webscraped.csv'],  # Specify the CSV file
    },
    install_requires=[
        'pandas',
    ],
)