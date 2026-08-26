BUREAU_PRIMARY_KEY: str | list[str] = "SK_ID_BUREAU"

BUREAU_UNIQUE_COLUMNS: list[str | list[str]] = ["SK_ID_BUREAU"]

BUREAU_DOMAIN_RULES = [

    # Identifiers
    {
        "type": "range",
        "column": "SK_ID_BUREAU",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "SK_ID_CURR",
        "min": 0,
        "allow_null": False,
    },

    # Credit status
    {
        "type": "allowed_values",
        "column": "CREDIT_ACTIVE",
        "values": ["Active", "Closed", "Sold", "Bad debt"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "CREDIT_CURRENCY",
        "values": ["currency 1", "currency 2", "currency 3", "currency 4"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "CREDIT_TYPE",
        "values": [
            "Another type of loan",
            "Car loan",
            "Cash loan (non-earmarked)",
            "Consumer credit",
            "Credit card",
            "Interbank credit",
            "Loan for business development",
            "Loan for purchase of shares (margin lending)",
            "Microloan",
            "Mobile operator loan",
            "Mortgage",
            "Unknown type of loan",
            'Loan for working capital replenishment',
            'Loan for the purchase of equipment',
            'Real estate loan'
        ],
        "allow_null": False,
    },

    # Credit timing

    # Number of days past due.
    {
        "type": "range",
        "column": "CREDIT_DAY_OVERDUE",
        "min": 0,
        "allow_null": False,
    },

    # Days before application when the credit bureau record was obtained.
    {
        "type": "range",
        "column": "DAYS_CREDIT",
        "max": 0,
        "allow_null": False,
    },

    # Scheduled credit end date relative to application.
    # Can be positive because the credit may extend beyond the application date.
    {
        "type": "range",
        "column": "DAYS_CREDIT_ENDDATE",
        "allow_null": True,
    },

    # Actual credit end date. XNA values are represented as NaN
    # in the numeric dataframe.
    {
        "type": "range",
        "column": "DAYS_ENDDATE_FACT",
        "max": 0,
        "allow_null": True,
    },

    # Last update of the bureau record.
    {
        "type": "range",
        "column": "DAYS_CREDIT_UPDATE",
        "max": 0,
        "allow_null": False,
    },

    # Credit amount
    {
        "type": "range",
        "column": "AMT_CREDIT_MAX_OVERDUE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_CREDIT_SUM",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_CREDIT_SUM_DEBT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_CREDIT_SUM_LIMIT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_CREDIT_SUM_OVERDUE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_ANNUITY",
        "min": 0,
        "allow_null": True,
    },

    # Credit prolongation
    {
        "type": "range",
        "column": "CNT_CREDIT_PROLONG",
        "min": 0,
        "allow_null": False,
    },
]

BUREAU_CONSISTENCY_RULES = [

    # Credit end date relationship
    #
    # DAYS_CREDIT is the starting point of the credit relative
    # to the application date. DAYS_ENDDATE_FACT is the actual closing date.
    #
    # Because both are negative day offsets: DAYS_ENDDATE_FACT >= DAYS_CREDIT
    # means the credit was closed after it was opened.

    {
        "type": "relationship",
        "name": "fact_enddate_after_credit_start",
        "rule": lambda df: df["DAYS_ENDDATE_FACT"].isna() | (df["DAYS_ENDDATE_FACT"] >= df["DAYS_CREDIT"])
    },

    # Credit update date cannot precede credit opening date.
    {
        "type": "relationship",
        "name": "credit_update_after_credit_start",
        "rule": lambda df: df["DAYS_CREDIT_UPDATE"] >= df["DAYS_CREDIT"]
    },

    # Actual overdue amount cannot exceed total outstanding debt.
    {
        "type": "relationship",
        "name": "overdue_vs_debt",
        "rule": lambda df: df["AMT_CREDIT_SUM_DEBT"].isna() | df["AMT_CREDIT_SUM_OVERDUE"].isna() | (df["AMT_CREDIT_SUM_OVERDUE"] <= df["AMT_CREDIT_SUM_DEBT"])
    },

    # Current debt should not exceed total credit amount.    
    {
        "type": "relationship",
        "name": "debt_vs_credit_sum",
        "rule": lambda df: df["AMT_CREDIT_SUM"].isna() | df["AMT_CREDIT_SUM_DEBT"].isna() | (df["AMT_CREDIT_SUM_DEBT"] <= df["AMT_CREDIT_SUM"])
    },

    # Overdue amount should not exceed total credit amount.
    {
        "type": "relationship",
        "name": "overdue_vs_credit_sum",
        "rule": lambda df: df["AMT_CREDIT_SUM"].isna() | df["AMT_CREDIT_SUM_OVERDUE"].isna() | (df["AMT_CREDIT_SUM_OVERDUE"] <= df["AMT_CREDIT_SUM"])
    },

    # If credit is Closed, there should normally be an actual end date.
    {
        "type": "relationship",
        "name": "closed_credit_has_end_date",
        "rule": lambda df: (df["CREDIT_ACTIVE"] != "Closed") | df["DAYS_ENDDATE_FACT"].notna()
    }
]