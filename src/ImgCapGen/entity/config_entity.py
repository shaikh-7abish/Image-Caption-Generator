from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class PrepareVGGConfig:
    root_dir: Path
    vgg_model_path: Path
 
@dataclass(frozen= True)
class PredictionConfig:
    tokenizer: Path
    model: Path

