import pandas as pd
from .report import CheckResult

def missing_summary(df: pd.DataFrame) -> pd.DataFrame:

    result = pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isna().sum().values,
        "total_count": len(df)
    })

    result["missing_rate"] = result["missing_count"] / result["total_count"]
    result["non_missing_count"] = result["total_count"] - result["missing_count"]
    result['dtype'] = [str(df[column].dtype) for column in df.columns]

    return result.sort_values("missing_rate", ascending=False).reset_index(drop=True)

def check_missing(df: pd.DataFrame, warning_threshold: float = 0.05, critical_threshold: float = 0.5) -> list[CheckResult]:
    summary = missing_summary(df)

    high_missing = summary[summary['missing_rate'] >= critical_threshold]
    medium_missing = summary[(summary['missing_rate'] < critical_threshold) & (summary["missing_rate"] >= warning_threshold)]

    result: list[CheckResult] = []

    if not high_missing.empty:
        result.append(
            CheckResult(
                check_name="missing_critical",
                status="WARNING",
                severity="HIGH",
                message=f"{len(high_missing)} columns have missing rate >= {critical_threshold:.0%}",
                details={
                    "columns": high_missing["column"].tolist(),
                    "missing_rates": dict(zip(high_missing["column"], high_missing["missing_rate"]))
                }
            )
        )
    else:
        result.append(
            CheckResult(
                check_name="missing_critical",
                status="PASS",
                message="No columns exceed the critical missing threshold."
            )
        )

    if not medium_missing.empty:
            result.append(
                CheckResult(
                    check_name="missing_warning",
                    status="WARNING",
                    severity="MEDIUM",
                    message=f"{len(medium_missing)} columns have missing rate between {warning_threshold:.0%} and {critical_threshold:.0%}.",
                    details={"columns": medium_missing["column"].tolist()}
                )
            )
    else:
        result.append(
            CheckResult(
                check_name="missing_critical",
                status="PASS",
                message="No columns exceed the warning missing threshold."
            )
        )
    return result

