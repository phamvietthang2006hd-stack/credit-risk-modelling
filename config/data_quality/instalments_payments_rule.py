INSTALMENTS_PAYMENTS_PRIMARY_KEY : str | list[str] = ['SK_ID_PREV', 'SK_ID_CURR', "NUM_INSTALMENT_VERSION","NUM_INSTALMENT_NUMBER"]

INSTALMENTS_PAYMENTS_UNIQUE_COLUMNS : list[str | list[str]] = []

INSTALMENTS_PAYMENTS_DOMAIN_RULES = [
    {
        'type': 'range',
        'column': 'SK_ID_PREV',
        'min': 0,
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'SK_ID_CURR',
        'min': 0,
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'NUM_INSTALMENT_VERSION',
        'min': 0,
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'NUM_INSTALMENT_NUMBER',
        'min': 0,
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'DAYS_INSTALMENT',
        'max': 0, 
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'DAYS_ENTRY_PAYMENT',
        'max': 0,
        'allow_null': True
    },

    {
        'type': 'range',
        'column': 'AMT_INSTALMENT',
        'min': 0, 
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'AMT_PAYMENT',
        'min': 0,
        'allow_null': True
    }
]

INSTALMENTS_PAYMENTS_CONSISTENCY_RULES = [
    {
        "type": "relationship",
        "name": "payment_date_vs_installment_date",
        "rule": lambda df: df["DAYS_ENTRY_PAYMENT"].isna() | (df["DAYS_ENTRY_PAYMENT"] >= df["DAYS_INSTALMENT"])
    }
]