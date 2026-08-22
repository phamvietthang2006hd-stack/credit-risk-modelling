from typing import Any, Callable
import pandas as pd
from .report import CheckResult

def check_numeric_range(df: pd.DataFrame, column: str, min_value: float | None = None, max_value: float | None = None, allow_null: bool = True) -> CheckResult:
    
    """Check if column is numeric"""

    series = df[column]

    if not pd.api.types.is_numeric_dtype(series):
        return CheckResult(
            check_name=f"domain_range_{column}",
            status="FAIL",
            severity="HIGH",
            message=f"Column '{column}' is not numeric.",
        )

    mask = pd.Series(False, index=df.index)

    if min_value is not None:
        mask |= series < min_value

    if max_value is not None:
        mask |= series > max_value

    if not allow_null:
        mask |= series.isna()

    invalid_count = int(mask.sum())

    if invalid_count > 0:
        return CheckResult(
            check_name=f"domain_range_{column}",
            status="FAIL",
            severity="HIGH",
            message=f"{invalid_count:,} invalid values detected in '{column}'.",
            details={
                "column": column,
                "min_value": min_value,
                "max_value": max_value,
                "invalid_count": invalid_count,
            },
        )

    return CheckResult(
        check_name=f"domain_range_{column}",
        status="PASS",
        message=f"Column '{column}' satisfies range constraints.",
    )


def check_allowed_values(df: pd.DataFrame, column: str, allowed_values: set[Any], allow_null: bool = True) -> CheckResult:

    """Check if column do not have all valid values."""

    series = df[column]

    mask = ~series.isin(allowed_values)

    if allow_null:
        mask &= series.notna()

    invalid_values = series[mask].drop_duplicates().tolist()

    if invalid_values:
        return CheckResult(
            check_name=f"domain_values_{column}",
            status="FAIL",
            severity="HIGH",
            message=f"Unexpected values detected in '{column}'.",
            details={
                "column": column,
                "allowed_values": list(allowed_values),
                "invalid_values": invalid_values,
                "invalid_count": int(mask.sum()),
            },
        )

    return CheckResult(
        check_name=f"domain_values_{column}",
        status="PASS",
        message=f"Column '{column}' contains valid domain values.",
    )


def check_custom_rule(df: pd.DataFrame, name: str, rule: Callable[[pd.DataFrame], pd.Series], severity: str = "HIGH") -> CheckResult:

    """Each table has itself rule. We can refer these rule in config/"""

    try:
        valid_mask = rule(df)

        if not isinstance(valid_mask, pd.Series):
            raise TypeError("Custom rule must return pandas Series.")

        invalid_count = int((~valid_mask).sum())

        if invalid_count > 0:
            return CheckResult(
                check_name=f"domain_custom_{name}",
                status="FAIL",
                severity=severity,
                message=f"Custom domain rule '{name}' failed for {invalid_count:,} rows.",
                details={"invalid_count": invalid_count},
            )

        return CheckResult(
            check_name=f"domain_custom_{name}",
            status="PASS",
            message=f"Custom domain rule '{name}' passed.",
        )

    except Exception as exc:
        return CheckResult(
            check_name=f"domain_custom_{name}",
            status="FAIL",
            severity="CRITICAL",
            message=f"Custom rule '{name}' could not be evaluated.",
            details={"error": str(exc)},
        )