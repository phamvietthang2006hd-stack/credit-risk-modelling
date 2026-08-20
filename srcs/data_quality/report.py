from dataclasses import field, dataclass
from typing import Any
import pandas as pd

@dataclass
class CheckResult:
    """
    Result of a data-quality check
    """

    check_name: str
    status: str 
    severity: str = "INFO"
    message: str = ""
    details: dict[str, Any] = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return self.status == "PASS"

    def to_dict(self) -> dict[str, Any]:
        return {
            "check_name": self.check_name,
            "status": self.status,
            "severity": self.severity,
            "message": self.message,
            "details": self.details
        }

class DataQualityReport:
    def __init__(self, dataset_name: str | None = None):
        self.dataset_name = dataset_name
        self.results: list[CheckResult] = []

    def add(self, check_name: str, status: str, severity: str = "INFO", message: str = "", details: dict[str, Any] | None = None) -> CheckResult:
        result = CheckResult(
            check_name=check_name,
            status=status,
            severity=severity,
            message=message,
            details=details or {},
        )
        self.results.append(result)
        return result

    def extend(self, results: list[CheckResult]) -> None:
        return self.results.extend(results)

    def to_dict(self) -> list[dict[str, Any]]:
        return [result.to_dict() for result in self.results]

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.to_dict())

    def summary(self) -> dict[str, int]:
        summary = {
            "total_check": len(self.results),
            "passed": 0,
            "failed": 0,
            "warnings": 0,
        }

        for result in self.results:
            if result.status == "PASS":
                summary["passed"] += 1
            elif result.status == "FAIL":
                summary["failed"] += 1
            elif result.status == "WARNING":
                summary["warnings"] += 1
        return summary

    def failed_check(self) -> list[CheckResult]:
        return [result for result in self.results if result.status == "FAIL"]

    def warning_check(self) -> list[CheckResult]:
        return [result for result in self.results if result.status == "WARNING"]

    def is_valid(self) -> bool:
        return not self.failed_check()

    def display(self) -> None:
        """Overall report"""

        summary = self.summary()
        print("=" * 70)
        print("DATA QUALITY REPORT")
        if self.dataset_name:
            print(f"Dataset: {self.dataset_name}")
        print("=" * 70)

        print(f"Total checks: {summary['total_check']}")
        print(f"Passed: {summary['passed']}")
        print(f"Failed: {summary['failed']}")
        print(f"Warnings: {summary['warnings']}")

        print ("-" * 70)

        for result in self.results:
            print(
                f"[{result.status}] "
                f"{result.check_name}: "
                f"{result.message}"
            )