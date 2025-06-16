import os, json
from jsonschema import validate, ValidationError
from dotenv import load_dotenv

load_dotenv()

DEFAULT_THRESHOLD = 80
SCHEMA = {
    "type": "object",
    "properties": {
        "alert_threshold": {"type": "integer", "minimum": 1, "maximum": 99}
    },
    "required": ["alert_threshold"]
}

# Load JSON config
with open('config.json') as f:
    cfg = json.load(f)
validate(cfg, SCHEMA)

# Allow ENV override
_threshold = os.getenv('ALERT_THRESHOLD')
if _threshold is not None:
    threshold = int(_threshold)
else:
    threshold = cfg['alert_threshold']

if not 1 <= threshold <= 99:
    raise ValueError(f"alert_threshold must be 1–99, got {threshold}")

ALERT_THRESHOLD = threshold
