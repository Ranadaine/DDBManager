# DDBManager

A simple DuckDB manager wrapper for Python that provides convenient methods for connecting to and querying DuckDB databases.

## Installation

```bash
pip install ddbmanager
```

## Usage

```python
from ddbmanager import DDBManager
import pandas as pd

# Create a manager instance
manager = DDBManager("my_database.duckdb")

# Execute a query
result = manager.query("SELECT * FROM my_table")
print(result)

# Query with parameters
result = manager.query("SELECT * FROM my_table WHERE id = ?", [1])

# Query with a pandas DataFrame
df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
result = manager.query("SELECT * FROM df WHERE col1 > 1", df=df)

# Print query results directly
manager.query_print("SELECT COUNT(*) FROM my_table")
```

## Features

- Simple connection management with automatic retry
- Support for parameterized queries
- Integration with pandas DataFrames
- Convenient result printing
- Built on DuckDB for high-performance analytics

## Requirements

- Python 3.7+
- DuckDB
- Pandas

## License

MIT License