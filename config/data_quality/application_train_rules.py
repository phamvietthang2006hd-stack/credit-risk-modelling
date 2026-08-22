PRIMARY_KEY = "SK_ID_CURR"

UNIQUE_COLUMNS: list[str | list[str]] = ["SK_ID_CURR"]

APPLICATION_TRAIN_DOMAIN_RULES = [

    # Target / ID
    {
        "type": "range",
        "column": "SK_ID_CURR",
        "min": 1,
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "TARGET",
        "values": [0, 1],
        "allow_null": False,
    },

    # Contract / demographic
    {
        "type": "allowed_values",
        "column": "NAME_CONTRACT_TYPE",
        "values": ["Cash loans", "Revolving loans"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "CODE_GENDER",
        "values": ["M", "F", "XNA"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_OWN_CAR",
        "values": ["Y", "N"],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_OWN_REALTY",
        "values": ["Y", "N"],
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "CNT_CHILDREN",
        "min": 0,
        "allow_null": False,
    },

    # Loan / income amounts
    {
        "type": "range",
        "column": "AMT_INCOME_TOTAL",
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
        "column": "AMT_ANNUITY",
        "min": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "AMT_GOODS_PRICE",
        "min": 0,
        "allow_null": True,
    },
    
    # Relative / age / date
    {
        "type": "range",
        "column": "REGION_POPULATION_RELATIVE",
        "min": 0,
        "max": 1,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "DAYS_BIRTH",
        "max": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "DAYS_REGISTRATION",
        "max": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "DAYS_ID_PUBLISH",
        "max": 0,
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "OWN_CAR_AGE",
        "min": 0,
        "allow_null": True,
    },

    # Binary flags

    {
        "type": "allowed_values",
        "column": "FLAG_MOBIL",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_EMP_PHONE",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_WORK_PHONE",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_CONT_MOBILE",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_PHONE",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "FLAG_EMAIL",
        "values": [0, 1],
        "allow_null": False,
    },

    # Family / region
    {
        "type": "range",
        "column": "CNT_FAM_MEMBERS",
        "min": 1,
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "REGION_RATING_CLIENT",
        "values": [1, 2, 3],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "REGION_RATING_CLIENT_W_CITY",
        "values": [1, 2, 3],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "WEEKDAY_APPR_PROCESS_START",
        "values": ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY","SATURDAY","SUNDAY"],
        "allow_null": False,
    },

    {
        "type": "range",
        "column": "HOUR_APPR_PROCESS_START",
        "min": 0,
        "max": 23,
        "allow_null": False,
    },

    # Region / city relationship flags
    {
        "type": "allowed_values",
        "column": "REG_REGION_NOT_LIVE_REGION",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "REG_REGION_NOT_WORK_REGION",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "LIVE_REGION_NOT_WORK_REGION",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "REG_CITY_NOT_LIVE_CITY",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "REG_CITY_NOT_WORK_CITY",
        "values": [0, 1],
        "allow_null": False,
    },

    {
        "type": "allowed_values",
        "column": "LIVE_CITY_NOT_WORK_CITY",
        "values": [0, 1],
        "allow_null": False,
    },

    # External source scores
    {
        "type": "range",
        "column": "EXT_SOURCE_1",
        "min": 0,
        "max": 1,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "EXT_SOURCE_2",
        "min": 0,
        "max": 1,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "EXT_SOURCE_3",
        "min": 0,
        "max": 1,
        "allow_null": True,
    },

    # Normalized building features
    *[
        {
            "type": "range",
            "column": column,
            "min": 0,
            "max": 1,
            "allow_null": True,
        }
        for column in [
            # AVG
            "APARTMENTS_AVG",
            "BASEMENTAREA_AVG",
            "YEARS_BEGINEXPLUATATION_AVG",
            "YEARS_BUILD_AVG",
            "COMMONAREA_AVG",
            "ELEVATORS_AVG",
            "ENTRANCES_AVG",
            "FLOORSMAX_AVG",
            "FLOORSMIN_AVG",
            "LANDAREA_AVG",
            "LIVINGAPARTMENTS_AVG",
            "LIVINGAREA_AVG",
            "NONLIVINGAPARTMENTS_AVG",
            "NONLIVINGAREA_AVG",

            # MODE
            "APARTMENTS_MODE",
            "BASEMENTAREA_MODE",
            "YEARS_BEGINEXPLUATATION_MODE",
            "YEARS_BUILD_MODE",
            "COMMONAREA_MODE",
            "ELEVATORS_MODE",
            "ENTRANCES_MODE",
            "FLOORSMAX_MODE",
            "FLOORSMIN_MODE",
            "LANDAREA_MODE",
            "LIVINGAPARTMENTS_MODE",
            "LIVINGAREA_MODE",
            "NONLIVINGAPARTMENTS_MODE",
            "NONLIVINGAREA_MODE",

            # MEDI
            "APARTMENTS_MEDI",
            "BASEMENTAREA_MEDI",
            "YEARS_BEGINEXPLUATATION_MEDI",
            "YEARS_BUILD_MEDI",
            "COMMONAREA_MEDI",
            "ELEVATORS_MEDI",
            "ENTRANCES_MEDI",
            "FLOORSMAX_MEDI",
            "FLOORSMIN_MEDI",
            "LANDAREA_MEDI",
            "LIVINGAPARTMENTS_MEDI",
            "LIVINGAREA_MEDI",
            "NONLIVINGAPARTMENTS_MEDI",
            "NONLIVINGAREA_MEDI",

            "TOTALAREA_MODE",
        ]
    ],

    # Social circle

    {
        "type": "range",
        "column": "OBS_30_CNT_SOCIAL_CIRCLE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DEF_30_CNT_SOCIAL_CIRCLE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "OBS_60_CNT_SOCIAL_CIRCLE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DEF_60_CNT_SOCIAL_CIRCLE",
        "min": 0,
        "allow_null": True,
    },

    {
        "type": "range",
        "column": "DAYS_LAST_PHONE_CHANGE",
        "max": 0,
        "allow_null": True,
    },

    # Document flags
    *[
        {
            "type": "allowed_values",
            "column": f"FLAG_DOCUMENT_{i}",
            "values": [0, 1],
            "allow_null": False,
        }
        for i in range(2, 22)
    ],

    # Credit bureau enquiry counts
    *[
        {
            "type": "range",
            "column": f"AMT_REQ_CREDIT_BUREAU_{suffix}",
            "min": 0,
            "allow_null": True,
        }
        for suffix in ["HOUR", "DAY", "WEEK", "MON", "QRT", "YEAR"]
    ],
]

APPLICATION_TRAIN_CONSISTENCY_RULES = [
    # Loan relationships

    {
        "type": "column_pair",
        "left": "AMT_CREDIT",
        "right": "AMT_GOODS_PRICE",
        "operator": "<=",
    },

    # Family relationship
    {
        "type": "relationship",
        "name": "family_members_vs_children",
        "rule": lambda df: (df["CNT_FAM_MEMBERS"] >= df["CNT_CHILDREN"] + 1)
    },

    # Employment days
    {
        "type": "relationship",
        "name": "days_employed_valid_encoding",
        "rule": lambda df: ((df["DAYS_EMPLOYED"] <= 0) | (df["DAYS_EMPLOYED"] == 365243))
    },

    {
        "type": "relationship",
        "name": "days_employed_anomaly_sentinel",
        "rule": lambda df: (df["DAYS_EMPLOYED"] != 365243)
    },


    # Social circle relationships
    {
        "type": "relationship",
        "name": "def_30_le_obs_30",
        "rule": lambda df: (df["DEF_30_CNT_SOCIAL_CIRCLE"] <= df["OBS_30_CNT_SOCIAL_CIRCLE"])
    },

    {
        "type": "relationship",
        "name": "def_60_le_obs_60",
        "rule": lambda df: (df["DEF_60_CNT_SOCIAL_CIRCLE"] <= df["OBS_60_CNT_SOCIAL_CIRCLE"])
    },

    # Region rating
    {
        "type": "relationship",
        "name": "region_rating_consistency",
        "rule": lambda df: (df["REGION_RATING_CLIENT"].isin([1, 2, 3]) & df["REGION_RATING_CLIENT_W_CITY"].isin([1, 2, 3]))
    },

    # Own car information
    {
        "type": "relationship",
        "name": "own_car_age_non_negative",
        "rule": lambda df: (df["OWN_CAR_AGE"].isna() | (df["OWN_CAR_AGE"] >= 0)),
    },

    # External source scores
    {
        "type": "relationship",
        "name": "external_sources_valid_range",
        "rule": lambda df: (
            (df["EXT_SOURCE_1"].isna() | df["EXT_SOURCE_1"].between(0, 1)) &
            (df["EXT_SOURCE_2"].isna() | df["EXT_SOURCE_2"].between(0, 1)) &
            (df["EXT_SOURCE_3"].isna() | df["EXT_SOURCE_3"].between(0, 1))
        ),
    },
]
