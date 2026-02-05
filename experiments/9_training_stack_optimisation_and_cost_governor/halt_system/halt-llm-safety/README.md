
# HALT LLM Safety System

Production-style automatic HALT controller designed to prevent runaway GPU spend during large-scale LLM training.

## Features
- Automatic checkpoint to S3 before termination
- Heartbeat stall detection
- NaN & divergence protection
- Throughput collapse detection
- GPU underutilization trigger
- Graceful halt + instance termination
- Orphan instance verification

## Repo Structure

```
halt-llm-safety/
├── trainer_node.py
├── halt_controller.py
├── requirements.txt
├── docs/
└── chaos/
```

## Quick Start

### 1. Install
```
pip install -r requirements.txt
```

### 2. Configure
Replace:

```
YOUR_BUCKET_NAME
```

in both scripts.

### 3. Run Controller (CPU EC2)
```
python halt_controller.py
```

### 4. Run Trainer (GPU EC2)
```
python trainer_node.py
```

Always chaos-test before expensive training runs.
