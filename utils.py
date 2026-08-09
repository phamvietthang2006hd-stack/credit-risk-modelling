from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = PROJECT_ROOT / "config" / "path.yaml"

class Config:
    def __init__(self, config_file: Path = CONFIG_PATH):
        self.project_root = PROJECT_ROOT
        with open(config_file, "r", encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

        self.data_dir = self.project_root / self.data.get("data_dir", "Home Credit Dataset")
        self.raw_dir = self.data_dir / self.data["dirs"]["raw"]
        self.train_dir = self.data_dir / self.data["dirs"]["train"]
        self.test_dir = self.data_dir / self.data["dirs"]["test"]

cfg = Config()