import pandas as pd
from typing import Any
import pandas as pd

from .report import CheckResult

def check_dataframe_structure(df: pd.DataFrame) -> list[CheckResult]:
    results: list[CheckResult] = []
    if not isinstance(df, pd.DataFrame):
        results.append(
            CheckResult(
                check_name="dataframe_type",
                status="FAIL", 
                severity="CRITICAL",
                message="Input is not a pandas DataFrame",
            )
        )
        return results

    results.append(
        CheckResult(
            check_name="dataframe_type",
            status="PASS",
            message="Input is a valid pandas DataFrame",
        )
    )

    # Shape:
    results.append(
        CheckResult(
            check_name="dataset_shape",
            status="PASS",
            message=f"Dataset contains {len(df):,} rows and {len(df.columns):,} columns.",
            details={
                "n_rows": len(df),
                "n_columns": len(df.columns)
            },
        )
    )

    # Empty dataset
    if df.empty:
        results.append(
            CheckResult(
                check_name="empty_dataset",
                status="FAIL",
                severity="CRITICAL",
                message="Dataset is empty",
            )
        )
    else:
        results.append(
            CheckResult(
                check_name="empty_dataset",
                status="PASS",
                message="Dataset contains observations.",
            )
        )

    # Empty column names
    empty_column_names = [str(column) for column in df.columns if str(column).strip() == ""]
    if empty_column_names:
        results.append(
            CheckResult(
                check_name="empty_column_names",
                status="FAIL",
                severity="HIGH",
                message="Empty column names detected.",
            )
        )
    else:
        results.append(
            CheckResult(
                check_name="empty_column_names",
                status="PASS",
                message="All columns have names.",
            )
        )

    # All-null columns:
    all_null_columns = [column for column in df.columns if df[column].isna().all()]
    if all_null_columns:
        results.append(
            CheckResult(
                check_name="all_null_columns",
                status="WARNING",
                severity="MEDIUM",
                message="Columns containing only missing values were detected",
            )
        )
    else:
        results.append(
            CheckResult(
                check_name="all_null_columns",
                status="PASS",
                message="No completely null columns."
            )
        )

    # Constant columns
    constant_columns = [column for column in df.columns if df[column].nunique(dropna=False) <= 1]
    if constant_columns:
        results.append(
            CheckResult(
                check_name="constant_columns",
                status="WARNING",
                severity="MEDIUM",
                message="Constant columns detected.",
                details={"columns": constant_columns},
            )
        )
    else:
        results.append(
            CheckResult(
                check_name="constant_columns",
                status="PASS",
                message="No constant columns.",
            )
        )

    return results