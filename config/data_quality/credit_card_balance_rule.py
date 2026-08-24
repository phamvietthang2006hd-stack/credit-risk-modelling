CREDIT_CARD_BALANCE_PRIMARY_KEY: str | list[str] = ["SK_ID_PREV", "MONTHS_BALANCE"]

CREDIT_CARD_BALANCE_UNIQUE_COLUMNS: list[str | list[str]] = []

CREDIT_CARD_BALANCE_DOMAIN_RULES = [

    {
        "type": "range",
        "column": "SK_ID_PREV",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "SK_ID_CURR",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "MONTHS_BALANCE",
        "max": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_BALANCE",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_CREDIT_LIMIT_ACTUAL",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_DRAWINGS_ATM_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_DRAWINGS_CURRENT",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_DRAWINGS_OTHER_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_DRAWINGS_POS_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_INST_MIN_REGULARITY",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_PAYMENT_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_PAYMENT_TOTAL_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_RECEIVABLE_PRINCIPAL",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_RECIVABLE",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_TOTAL_RECEIVABLE",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "CNT_DRAWINGS_ATM_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "CNT_DRAWINGS_CURRENT",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "CNT_DRAWINGS_OTHER_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "CNT_DRAWINGS_POS_CURRENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "CNT_INSTALMENT_MATURE_CUM",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "CNT_INSTALMENT_MATURE_CUM",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "SK_DPD",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "SK_DPD_DEF",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NAME_CONTRACT_STATUS",
        "values": [
            "Active",
            "Completed",
            "Demand",
            "Signed",
            "Sent proposal",
            "Refused",
            "Approved"
        ],
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "CNT_INSTALMENT_MATURE_CUM",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_INST_MIN_REGULARITY",
        "min": 0,
        "allow_null": True,
    },
]

CREDIT_CARD_BALANCE_CONSISTENCY_RULES = [

    {
        "type": "relationship",
        "name": "drawings_components_vs_total",
        "rule": lambda df: df[["AMT_DRAWINGS_ATM_CURRENT", "AMT_DRAWINGS_OTHER_CURRENT", "AMT_DRAWINGS_POS_CURRENT"]].isna().any(axis=1)
                | (df["AMT_DRAWINGS_ATM_CURRENT"] + df["AMT_DRAWINGS_OTHER_CURRENT"] + df["AMT_DRAWINGS_POS_CURRENT"] == df["AMT_DRAWINGS_CURRENT"])
    },

    {
        "type": "relationship",
        "name": "drawing_counts_components_vs_total",
        "rule": lambda df: (df[["CNT_DRAWINGS_ATM_CURRENT","CNT_DRAWINGS_OTHER_CURRENT","CNT_DRAWINGS_POS_CURRENT"]].isna().any(axis=1)
            | (df["CNT_DRAWINGS_ATM_CURRENT"] + df["CNT_DRAWINGS_OTHER_CURRENT"] + df["CNT_DRAWINGS_POS_CURRENT"] == df["CNT_DRAWINGS_CURRENT"])
        ),
    },

    {
        "type": "relationship",
        "name": "payment_current_vs_payment_total",
        "rule": lambda df: df["AMT_PAYMENT_CURRENT"].isna() | df["AMT_PAYMENT_TOTAL_CURRENT"].isna() | (df["AMT_PAYMENT_CURRENT"] <= df["AMT_PAYMENT_TOTAL_CURRENT"]),
    },

    {
        "type": "relationship",
        "name": "receivable_principal_vs_total",
        "rule": lambda df: df["AMT_RECEIVABLE_PRINCIPAL"] <= df["AMT_TOTAL_RECEIVABLE"]
    },

    {
        "type": "relationship",
        "name": "receivable_vs_total_receivable",
        "rule": lambda df: df["AMT_RECIVABLE"] <= df["AMT_TOTAL_RECEIVABLE"]
    },

    {
        "type": "relationship",
        "name": "dpd_def_vs_dpd",
        "rule": lambda df: df["SK_DPD_DEF"] <= df["SK_DPD"]
    },

    {
        "type": "relationship",
        "name": "balance_vs_credit_limit",
        "rule": lambda df: df["AMT_BALANCE"] <= df["AMT_CREDIT_LIMIT_ACTUAL"]
    },
]