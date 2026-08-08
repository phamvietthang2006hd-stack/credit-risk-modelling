from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

class DataSplitDistributor:
    """Split Home Credit Data and distribute table to train/test folders"""

    TABLES = (
        "application_train",
        "bureau",
        "previous_application",
        "credit_card_balance",
        "POS_CASH_balance",
        "installments_payments"
    )

    def __init__(
        self,
        raw_data_dir: str | Path,
        interim_data_dir: str | Path,
        test_size: float = 0.2,
        random_state: int = 42
    ) -> None:
        self.raw_dir: Path = Path(raw_data_dir)
        self.interim_dir: Path = Path(interim_data_dir)
        self.train_dir = self.interim_dir / "train"
        self.test_dir = self.interim_dir / "test"

        self.test_size = test_size
        self.random_state = random_state

        self.train_ids : set[int] = set()
        self.test_ids : set[int] = set()

        self._train_bureau_ids: set[int] = set()
        self._test_bureau_ids: set[int] = set()

    def run(self) -> None:
        """Execute the complete split-distribute pipeline."""
        self._prepare_directories()

        application = self._load_application()
        self._split_ids(application)
        self._distribute_tables()
        self._distribute_bureau_balance()
        self._validate(application)

    def _prepare_directories(self) -> None:
        """Create output directories if they do not exist."""
        self.train_dir.mkdir(parents=True, exist_ok=True)
        self.test_dir.mkdir(parents=True, exist_ok=True)

    def _load_application(self) -> pd.DataFrame:
        return pd.read_csv(self.raw_dir / "application_train.csv")

    def _split_ids(self, application: pd.DataFrame) -> None:
        train_df, test_df = train_test_split(
            application,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=application["TARGET"]
        )
        self.train_ids = set(train_df["SK_ID_CURR"])
        self.test_ids = set(test_df["SK_ID_CURR"])

    def _distribute_tables(self) -> None:
        for table in self.TABLES:
            df = pd.read_csv(self.raw_dir / f"{table}.csv")
            train_df, test_df = self._filter_by_curr_id(df)

            # Lưu lại bureau IDs trực tiếp trên memory
            if table == "bureau":
                self._train_bureau_ids = set(train_df["SK_ID_BUREAU"])
                self._test_bureau_ids = set(test_df["SK_ID_BUREAU"])

            train_df.to_csv(self.train_dir / f"{table}.csv", index=False)
            test_df.to_csv(self.test_dir / f"{table}.csv", index=False)

    def _distribute_bureau_balance(self) -> None:
        """Distribute bureau_balance.csv using cached bureau IDs."""
        bureau_balance_path = self.raw_dir / "bureau_balance.csv"
        if not bureau_balance_path.exists():
            return

        bureau_balance = pd.read_csv(bureau_balance_path)

        bureau_balance[
            bureau_balance["SK_ID_BUREAU"].isin(self._train_bureau_ids)
        ].to_csv(self.train_dir / "bureau_balance.csv", index=False)

        bureau_balance[
            bureau_balance["SK_ID_BUREAU"].isin(self._test_bureau_ids)
        ].to_csv(self.test_dir / "bureau_balance.csv", index=False)

    def _filter_by_curr_id(
        self, df: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        train_df = df[df["SK_ID_CURR"].isin(self.train_ids)]
        test_df = df[df["SK_ID_CURR"].isin(self.test_ids)]
        return train_df, test_df

    def _validate(self, application: pd.DataFrame) -> None:
        train = application[application["SK_ID_CURR"].isin(self.train_ids)]
        test = application[application["SK_ID_CURR"].isin(self.test_ids)]

        print("-" * 50)
        print(f"Train customers : {len(train):,}")
        print(f"Test customers  : {len(test):,}")
        print(f"Train default   : {train['TARGET'].mean():.4f}")
        print(f"Test default    : {test['TARGET'].mean():.4f}")
        print(f"Overlap         : {len(self.train_ids & self.test_ids)}")
        print("-" * 50)
