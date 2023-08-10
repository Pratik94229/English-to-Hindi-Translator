from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: str
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    tokenizer_name: Path
    source: str
