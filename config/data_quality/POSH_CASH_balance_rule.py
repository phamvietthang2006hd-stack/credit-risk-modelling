POS_CASH_PRIMARY_KEY : str | list[str] = ['SK_ID_PREV', 'SK_ID_CURR']

POSH_CASH_UNIQUE_COLUMNS : list[str | list[str]] = []

POSH_CASH_DOMAIN_RULES = [

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
        'column': 'MONTHS_BALANCE',
        'max': 0,
        'allow_null': False
    },

    {
        'type': 'range',
        'column': 'CNT_INSTALMENT',
        'min': 0,
        'allow_null': True
    },

    {
        'type': 'range',
        'column': 'CNT_INSTALMENT_FUTURE',
        'min': 0,
        'allow_null': True
    },

    {
        'type': 'allowed_values',
        'column': 'NAME_CONTRACT_STATUS',
        'values': [
            'Active',
            'Completed',
            'Signed',
            'Demand',
            'Returned to the store',
            'Approved',
            'Amortized debt',
            'Canceled',
            'XNA'
        ]
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
    }
]

POS_CASH_CONSISTENCY_RULES = [

    {
        'type': 'relationship',
        'name': 'future_installments_vs_installments',
        'rule': lambda df: df['CNT_INSTALMENT'].isna() | df['CNT_INSTALMENT_FUTURE'].isna() | (df['CNT_INSTALMENT'] >= df['CNT_INSTALMENT_FUTURE']),
    }, 

    {
        "type": "relationship",
        "name": "dpd_def_vs_dpd",
        "rule": lambda df: df["SK_DPD_DEF"] <= df["SK_DPD"]
    },

    {
        "type": "relationship",
        "name": "completed_contract_no_future_installments",
        "rule": lambda df: (df["NAME_CONTRACT_STATUS"] != "Completed") | df["CNT_INSTALMENT_FUTURE"].isna() | (df["CNT_INSTALMENT_FUTURE"] == 0)
    },
]

    
