# Runbook: Linux Filesystem Usage High

## Symptom
Grafana alert: filesystem usage above 85% or 95%.

## Impact
If `/` is full, services may fail:
- VS Code Remote-SSH
- Cockpit
- PackageKit
- systemd services
- Docker logs

## Check current usage

```bash
df -h
df -i
