# Historical Earnings Package

This package allows you to query historical earnings report dates for stock tickers over a specified time range.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/historical_earnings_package.git
    ```

2. Install the package:
    ```
    pip install .
    ```

## Usage

```python
from historical_earnings_package import load_earnings_data, get_earnings_dates

# Load the earnings data from a CSV file
data = load_earnings_data('path/to/your/data/aggregated_earnings_data_webscraped.csv')

# Query earnings for AAPL between 2020 and 2021
earnings = get_earnings_dates('AAPL', '2020-01-01', '2021-12-31', data)
print(earnings)
