
# Trigger Thresholds

## Priority 0 (Immediate Kill)
- NaN / Inf loss
- Loss divergence (>5× moving avg)

## Priority 1
- Heartbeat stall (>120s)
- Throughput drop (>50%)
- GPU utilization <20%

Designed to prevent silent multi-day GPU burn.
