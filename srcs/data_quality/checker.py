from typing import Any, Callable
import pandas as pd

from .consistency import check_column_pair, check_relationship
from .domain import check_allowed_values, check_custom_rule, check_numeric_range
from .duplicate import check_duplicate_rows, check_primary_key, check_unique_columns
from .missing import check_missing, missing_summary
from .structure import check_dataframe_structure
from .report import DataQualityReport


class DataQualityChecker:
    """Main interface for data-quality framework."""

    def __init__(self, df: pd.DataFrame, dataset_name: str | None = None):
        self.df = df
        self.dataset_name = dataset_name

    def run(
        self,
        primary_key: str | list[str] | None = None,
        unique_columns: list[str | list[str]] | None = None,
        domain_rules: list[dict[str, Any]] | None = None,
        consistency_rules: list[dict[str, Any]] | None = None,
        missing_warning_threshold: float = 0.05,
        missing_critical_threshold: float = 0.3,
    ) -> DataQualityReport:

        report = DataQualityReport(dataset_name=self.dataset_name)

        # 1. Structure
        report.extend(check_dataframe_structure(self.df))

        # 2. Missing values
        report.extend(check_missing(self.df, warning_threshold=missing_warning_threshold, critical_threshold=missing_critical_threshold))

        # 3. Duplicates
        report.extend(check_duplicate_rows(self.df))

        # 4. Primary key
        if primary_key:
            report.extend(check_primary_key(self.df, primary_key))

        # 5. Other unique columns
        if unique_columns:
            for columns in unique_columns:
                report.extend(check_unique_columns(self.df, columns))

        # 6. Domain rules
        if domain_rules:
            for rule in domain_rules:
                rule_type = rule.get("type")

                if rule_type == "range":
                    result = check_numeric_range(
                        self.df,
                        column=rule["column"],
                        min_value=rule.get("min"),
                        max_value=rule.get("max"),
                        allow_null=rule.get("allow_null", True)
                    )
                    report.results.append(result)

                elif rule_type == "allowed_values":
                    result = check_allowed_values(
                        self.df,
                        column=rule["column"],
                        allowed_values=set(rule["values"]),
                        allow_null=rule.get("allow_null", True),
                    )
                    report.results.append(result)

                elif rule_type == "custom":
                    result = check_custom_rule(
                        self.df,
                        name=rule["name"],
                        rule=rule["rule"],
                        severity=rule.get("severity", "HIGH"),
                    )
                    report.results.append(result)

                else:
                    raise ValueError(f"Unsupported domain rule type: {rule_type}")

        # 7. Consistency rules
        if consistency_rules:
            for rule in consistency_rules:

                rule_type = rule.get("type")

                if rule_type == "relationship":
                    result = check_relationship(
                        self.df,
                        name=rule["name"],
                        rule=rule["rule"],
                        severity=rule.get("severity", "HIGH"),
                    )

                elif rule_type == "column_pair":

                    result = check_column_pair(
                        self.df,
                        left_column=rule["left"],
                        right_column=rule["right"],
                        operator=rule["operator"],
                    )

                else:
                    raise ValueError(f"Unsupported consistency rule type: {rule_type}")

                report.results.append(result)

        return report

    def missing_report(self) -> pd.DataFrame:
        return missing_summary(self.df)

    def profile(self) -> pd.DataFrame:
        """Statistical profile"""

        rows = []

        for column in self.df.columns:

            series = self.df[column]

            row = {
                "column": column,
                "dtype": str(series.dtype),
                "n_rows": len(series),
                "n_unique": series.nunique(dropna=True),
                "missing_count": int(series.isna().sum()),
                "missing_rate": float(series.isna().mean())
            }

            if pd.api.types.is_numeric_dtype(series):

                row.update({
                    "min": series.min(),
                    "max": series.max(),
                    "mean": series.mean(),
                    "median": series.median(),
                    "std": series.std(),
                })

            rows.append(row)

        return pd.DataFrame(rows)