from typing import Callable
import pandas as pd
from .report import CheckResult


def check_relationship(df: pd.DataFrame, name: str, rule: Callable[[pd.DataFrame], pd.Series], severity: str = "HIGH") -> CheckResult:

    """Check the logic of each column"""

    try:
        valid_mask = rule(df)

        if not isinstance(valid_mask, pd.Series):
            raise TypeError("Consistency rule must return pandas Series.")

        invalid_mask = ~valid_mask.fillna(True)
        invalid_count = int(invalid_mask.sum())

        if invalid_count > 0:
            return CheckResult(
                check_name=f"consistency_{name}",
                status="FAIL",
                severity=severity,
                message=f"Consistency rule '{name}' failed for {invalid_count:,} rows.",
                details={"invalid_count": invalid_count},
            )

        return CheckResult(
            check_name=f"consistency_{name}",
            status="PASS",
            message=f"Consistency rule '{name}' passed.",
        )

    except Exception as exc:
        return CheckResult(
            check_name=f"consistency_{name}",
            status="FAIL",
            severity="CRITICAL",
            message=f"Consistency rule '{name} could not be evaluated.",
            details={"error": str(exc)},
        )


def check_column_pair(df: pd.DataFrame, left_column: str, right_column: str, operator: str) -> CheckResult:

    """Check relationship between 2 fields"""

    required_columns = {left_column, right_column}

    missing = [column for column in required_columns if column not in df.columns]

    name = f"{left_column}_{operator}_{right_column}"

    if missing:
        return CheckResult(
            check_name=f"consistency_{name}",
            status="FAIL",
            severity="HIGH",
            message="Required columns are missing.",
            details={"missing_columns": missing},
        )

    left = df[left_column]
    right = df[right_column]

    if operator == ">=":
        valid = left >= right
    elif operator == ">":
        valid = left > right
    elif operator == "<=":
        valid = left <= right
    elif operator == "<":
        valid = left < right
    elif operator == "==":
        valid = left == right
    elif operator == "!=":
        valid = left != right
    else:
        raise ValueError(f"Unsupported operator: {operator}")

    invalid_count = int((~valid.fillna(True)).sum())

    if invalid_count:
        return CheckResult(
            check_name=f"consistency_{name}",
            status="FAIL",
            severity="HIGH",
            message=f"{left_column} {operator} {right_column} violated by {invalid_count:,} rows.",
            details={
                "left_column": left_column,
                "right_column": right_column,
                "operator": operator,
                "invalid_count": invalid_count,
            }
        )

    return CheckResult(
        check_name=f"consistency_{name}",
        status="PASS",
        message=f"{left_column} {operator} {right_column} is satisfied."
    )