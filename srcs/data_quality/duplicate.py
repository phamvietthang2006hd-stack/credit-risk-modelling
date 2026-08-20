import pandas as pd
from .report import CheckResult

def check_duplicate_rows(df: pd.DataFrame) -> list[CheckResult]:

    duplicate_mask = df.duplicated(keep=False)
    duplicate_count = int(duplicate_mask.sum())

    if duplicate_count > 0:
        return [
            CheckResult(
                check_name="duplicate_rows",
                status="WARNING",
                severity="MEDIUM",
                message=f"{duplicate_count:,} rows are duplicated.",
                details={
                    "duplicate_rows": duplicate_count,
                    "duplicate_groups": int(df[duplicate_mask].drop_duplicates().shape[0])
                }
            )
        ]
    return [
        CheckResult(
            check_name="duplicate_rows",
            status="PASS",
            message="No duplicated rows detected."
        )
    ]

def check_unique_columns(df: pd.DataFrame, columns: str | list[str]) -> list[CheckResult]:

    duplicate_mask = df.duplicated(subset=columns, keep=False)
    duplicate_count = int(duplicate_mask.sum())

    if duplicate_count > 0:
        return [
            CheckResult(
                check_name="unique_columns",
                status="FAIL",
                severity="HIGH",
                message=f"Uniqueness violation detected in f{columns}",
                details={
                    "columns": columns,
                    "duplicate_rows": duplicate_count
                }
            )
        ]

    return [
            CheckResult(
                check_name="unique_columns",
                status="PASS",
                message=f"Columns {columns} are unique.",
                details={"columns": columns}
            )
        ]

def check_primary_key(df: pd.DataFrame, primary_key: str | list[str]) -> list[CheckResult]:
    if isinstance(primary_key, str):
        primary_key = [primary_key]
    missing_columns = [column for column in primary_key if column not in df.columns]
    if missing_columns:
        return [
            CheckResult(
                check_name="primary_key",
                status='FAIL',
                severity="CRITICAL",
                message="Primary key columns are missing",
                details={"missing_columns": missing_columns}
            )
        ]

    results = []

    null_mask = df[primary_key].isna().any(axis=1)
    null_count= int(null_mask.sum())

    if null_count > 0:
        results.append(
            CheckResult(
                check_name="primary_key_null",
                status='FAIL',
                severity="CRITICAL",
                message=f"Primary key contains {null_count:,} null rows.",
                details={
                    "null_rows": null_count,
                    "columns": primary_key
                }
            )
        )
    else:
        results.append(
            CheckResult(
                check_name="primary_key_null",
                status="PASS",
                message="Primary key contains no null values."
            )
        )

    duplicate_mask = df.duplicated(subset=primary_key, keep=False)
    duplicate_count = int(duplicate_mask.sum())

    if duplicate_count > 0:
        results.append(
            CheckResult(
                check_name="primary_key_unique",
                status="FAIL",
                severity="CRITICAL",
                message="Primary key is not unique: {duplicate_count:,} rows involved.",
                details={
                    "duplicate_rows": duplicate_count,
                    "columns": primary_key
                }
            )
        )

    else:
        results.append(
            CheckResult(
                check_name="primary_key_unique",
                status="PASS",
                message="Primary key is unique."
            )
        )
    return results