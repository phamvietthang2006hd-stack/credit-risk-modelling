from srcs.data_quality.checker import DataQualityChecker
import pandas as pd
from typing import Any
from IPython.display import display

def check_df(
        df: pd.DataFrame,
        dataset: str,
        primary_key: str | list[str],
        unique_columns: list[str | list[str]],
        domain_rule: list[dict[str, Any]],
        consistency_rule: list[dict[str, Any]]
) -> DataQualityChecker:
    checker = DataQualityChecker(df=df, dataset_name=dataset)

    report = checker.run(
        primary_key=primary_key,
        unique_columns=unique_columns,
        domain_rules=domain_rule,
        consistency_rules=consistency_rule
    )

    # Summary of report
    print(f'Summary: {report.summary()}')
    print("=" * 50)
    
    # FAIL/WARNING check
    dq_result = report.to_dataframe()
    print("FAIL/WARNING check")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
        display(dq_result[dq_result['status'] != 'PASS'])
    print("=" * 50)

    # Missing report
    missing_report = checker.missing_report()
    print("Missing report:")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
        display(missing_report[missing_report['missing_count'] > 0])
    print("=" * 50)

    # Profile
    profile = checker.profile()
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
        display(profile)

    return checker