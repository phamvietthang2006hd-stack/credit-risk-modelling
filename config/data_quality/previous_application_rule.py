PREVIOUS_APPLICATION_PRIMARY_KEY: str | list[str] = "SK_ID_PREV"

PREVIOUS_APPLICATION_UNIQUE_COLUMNS: list[str | list[str]] = ["SK_ID_PREV"]

PREVIOUS_APPLICATION_DOMAIN_RULES = [

    # Identifiers
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

    # Credit Amount
    {
        "type": "range",
        "column": "AMT_ANNUITY",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_APPLICATION",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_CREDIT",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_DOWN_PAYMENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "AMT_GOODS_PRICE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "RATE_DOWN_PAYMENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "RATE_INTEREST_PRIMARY",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "RATE_INTEREST_PRIVILEGED",
        "min": 0,
        "allow_null": True,
    },

    # Term / payment information
    {
        "type": "range",
        "column": "CNT_PAYMENT",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_FIRST_DRAWING",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_FIRST_DUE",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_LAST_DUE_1ST_VERSION",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_LAST_DUE",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_TERMINATION",
        "max": 0,
        "allow_null": True,
    },

    # Decision / process information
    {
        "type": "range",
        "column": "DAYS_DECISION",
        "max": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "HOUR_APPR_PROCESS_START",
        "min": 0,
        "max": 23,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "WEEKDAY_APPR_PROCESS_START",
        "min": 0,
        "max": 6,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "SELLERPLACE_AREA",
        "min": -1,
        "allow_null": False,
    },

    # Binary flags
    {
        "type": "allowed_values",
        "column": "FLAG_LAST_APPL_PER_CONTRACT",
        "values": ["Y", "N"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NFLAG_LAST_APPL_IN_DAY",
        "values": [0, 1],
        "allow_null": False,
    },
    
    {
        "type": "allowed_values",
        "column": "NFLAG_INSURED_ON_APPROVAL",
        "values": [0, 1],
        "allow_null": True,
    },

    # Contract status
    {
        "type": "allowed_values",
        "column": "NAME_CONTRACT_STATUS",
        "values": ["Approved","Cancelled", "Refused","Unused offer"],
        "allow_null": False,
    },

    # Contract type
    {
        "type": "allowed_values",
        "column": "NAME_CONTRACT_TYPE",
        "values": ["Cash loans", "Consumer loans", "Revolving loans", "XNA"],
        "allow_null": False,
    },

    # Payment / yield group
    {
        "type": "allowed_values",
        "column": "NAME_YIELD_GROUP",
        "values": ["low_action", "low_normal", "middle", "high", "XNA"],
        "allow_null": False,
    },

    # Product combination
    {
        "type": "allowed_values",
        "column": "PRODUCT_COMBINATION",
        "values": [
            "Card Street",
            "Card X-Sell",
            "Cash",
            "Cash Street",
            "Cash X-Sell",
            "POS household with interest",
            "POS household without interest",
            "POS mobile with interest",
            "POS mobile without interest",
            "POS other with interest",
            "POS other without interest",
            "POS industry with interest",
            "POS industry without interest",
        ],
        "allow_null": True,
    },

    # Client information
    {
        "type": "allowed_values",
        "column": "NAME_CLIENT_TYPE",
        "values": ["New", "Refreshed", "Repeater", "XNA"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NAME_GOODS_CATEGORY",
        "values": [
            "Additional Service",
            "Animals",
            "Audio/Video",
            "Auto Accessories",
            "Clothing and Accessories",
            "Computers",
            "Construction Materials",
            "Consumer Electronics",
            "Direct Sales",
            "Education",
            "Fitness",
            "Furniture",
            "Gardening",
            "Homewares",
            "Industry",
            "Jewelry",
            "Medical Supplies",
            "Medicine",
            "Mobile",
            "Office Appliances",
            "Other",
            "Photo / Cinema Equipment",
            "Sport and Leisure",
            "Tourism",
            "Vehicles",
            "Weapon",
            "XNA",
        ],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NAME_PAYMENT_TYPE",
        "values": ["Cash through the bank", "Cashless from the account", "Non-cash from your account", "XNA"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NAME_PORTFOLIO",
        "values": ["Cards","Cash","POS","XNA"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NAME_PRODUCT_TYPE",
        "values": ["x-sell", "walk-in", "XNA"],
        "allow_null": False,
    },

    # Channel / sales information
    {
        "type": "allowed_values",
        "column": "CHANNEL_TYPE",
        "values": [
            "AP+ (Cash loan)",
            "Car dealer",
            "Channel of corporate sales",
            "Contact center",
            "Country-wide",
            "Credit and cash offices",
            "Regional / Local",
            "Stone",
        ],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "NAME_SELLER_INDUSTRY",
        "values": [
            "Auto technology",
            "Clothing",
            "Connectivity",
            "Construction",
            "Consumer electronics",
            "Furniture",
            "Industry",
            "Jewelry",
            "MLM partners",
            "Tourism",
            "XNA",
        ],
        "allow_null": False,
    },

    # Cash / installment information
    {
        "type": "range",
        "column": "SELLERPLACE_AREA",
        "min": -1,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "DAYS_FIRST_DRAWING",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_FIRST_DUE",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_LAST_DUE_1ST_VERSION",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_LAST_DUE",
        "max": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_TERMINATION",
        "max": 0,
        "allow_null": True,
    },
]

PREVIOUS_APPLICATION_CONSISTENCY_RULES = [

    # Credit amount should not exceed requested application amount.
    {
        "type": "column_pair",
        "left": "AMT_APPLICATION",
        "right": "AMT_CREDIT",
        "operator": ">=",
    },

    # Down payment cannot exceed the application amount.
    {
        "type": "relationship",
        "name": "down_payment_vs_application",
        "rule": lambda df: df["AMT_DOWN_PAYMENT"].isna() | df["AMT_APPLICATION"].isna() | (df["AMT_DOWN_PAYMENT"] <= df["AMT_APPLICATION"])
    },

    # Annuity should be positive when a payment count exists.
    {
        "type": "relationship",
        "name": "annuity_vs_payment_count",
        "rule": lambda df: df["CNT_PAYMENT"].isna() | df["AMT_ANNUITY"].isna() | (df["CNT_PAYMENT"] == 0) | (df["AMT_ANNUITY"] > 0)
    },

    # First due date cannot occur before first drawing.
    # Both values are represented as negative day offsets.
    {
        "type": "relationship",
        "name": "first_due_after_first_drawing",
        "rule": lambda df: df["DAYS_FIRST_DRAWING"].isna() | df["DAYS_FIRST_DUE"].isna() | (df["DAYS_FIRST_DUE"] >= df["DAYS_FIRST_DRAWING"])
    },

    # Last due date should not occur before first due date.
    {
        "type": "relationship",
        "name": "last_due_after_first_due",
        "rule": lambda df: df["DAYS_FIRST_DUE"].isna() | df["DAYS_LAST_DUE"].isna() | (df["DAYS_LAST_DUE"] >= df["DAYS_FIRST_DUE"])
    },

    # Last due date of the first version should not occur before first due date.
    {
        "type": "relationship",
        "name": "last_due_1st_version_after_first_due",
        "rule": lambda df: df["DAYS_FIRST_DUE"].isna() | df["DAYS_LAST_DUE_1ST_VERSION"].isna() | (df["DAYS_LAST_DUE_1ST_VERSION"] >= df["DAYS_FIRST_DUE"])
    },

    # Termination should not occur before first due date.
    {
        "type": "relationship",
        "name": "termination_after_first_due",
        "rule": lambda df: df["DAYS_FIRST_DUE"].isna() | df["DAYS_TERMINATION"].isna()| (df["DAYS_TERMINATION"] >= df["DAYS_FIRST_DUE"])
    },
]