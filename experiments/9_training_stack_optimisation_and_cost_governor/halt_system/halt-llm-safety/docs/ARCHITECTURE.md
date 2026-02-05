
# HALT Architecture

Controller runs on a CPU EC2 instance separate from training nodes.

## Flow

Trigger → Force Checkpoint → Confirm S3 `_SUCCESS` → Terminate EC2 → Verify No Orphans

Compute is NEVER terminated before checkpoint confirmation.
