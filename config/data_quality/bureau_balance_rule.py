BUREAU_BALANCE_PRIMARY_KEY: str | list[str] = ['SK_ID_BUREAU', 'MONTHS_BALANCE']

BUREAU_BALANCE_UNIQUE_COLUMNS: list[str | list[str]] = []

BUREAU_BALANCE_DOMAIN_RULES = [

    # Identifier
    {
        "type": "range",
        "column": "SK_ID_BUREAU",
        "min": 0,
        "allow_null": False,
    },

    # Month relative to application
    {
        "type": "range",
        "column": "MONTHS_BALANCE",
        "max": 0,
        "allow_null": False,
    },

    # Monthly credit status
    {
        "type": "allowed_values",
        "column": "STATUS",
        "values": ["0", "1", "2", "3", "4", "5", "C", "X"],
        "allow_null": False,
    },
]

BUREAU_BALANCE_CONSISTENCY_RULES = []
