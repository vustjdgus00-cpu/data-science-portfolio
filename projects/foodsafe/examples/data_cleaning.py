"""Selected generic preprocessing functions from FOODSAFE.
No source records, linkage rules or dashboard logic are included.
"""
import pandas as pd


def normalize_text(frame: pd.DataFrame) -> pd.DataFrame:
    """Normalize string cells and remove only byte-for-byte duplicate records."""
    result = frame.copy()
    for column in result.select_dtypes(include=["object", "string"]):
        result[column] = result[column].str.strip().replace("", pd.NA)
    return result.drop_duplicates().reset_index(drop=True)


def add_date(frame: pd.DataFrame, source_column: str, output_column: str) -> pd.DataFrame:
    result = frame.copy()
    result[output_column] = pd.to_datetime(result[source_column], errors="coerce").dt.strftime("%Y-%m-%d")
    return result
