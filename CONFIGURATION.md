# Configuration Guide

This document describes the configuration options available for ZONE-GPT.

## Environment Variables

ZONE-GPT can be configured using the following environment variables:

### Application Settings

#### `ALLOWED_ORIGINS`
- **Description**: Comma-separated list of allowed CORS origins
- **Default**: `*` (allows all origins - NOT RECOMMENDED for production)
- **Example**: `ALLOWED_ORIGINS=https://app.example.com,https://admin.example.com`
- **Security Note**: In production, always specify exact origins instead of using `*`

### Server Configuration

#### `ZONE_GPT_HOST`
- **Description**: Host address to bind the server to
- **Default**: `0.0.0.0` (listens on all interfaces)
- **Example**: `ZONE_GPT_HOST=127.0.0.1` (localhost only)

#### `ZONE_GPT_PORT`
- **Description**: Port number for the server
- **Default**: `8000`
- **Example**: `ZONE_GPT_PORT=8080`

#### `ZONE_GPT_RELOAD`
- **Description**: Enable auto-reload on code changes (development only)
- **Default**: `false`
- **Values**: `true`, `1`, `yes` (enable) / `false`, `0`, `no` (disable)
- **Example**: `ZONE_GPT_RELOAD=true`
- **Security Note**: Never enable in production

#### `ZONE_GPT_LOG_LEVEL`
- **Description**: Logging level for the application
- **Default**: `info`
- **Values**: `debug`, `info`, `warning`, `error`, `critical`
- **Example**: `ZONE_GPT_LOG_LEVEL=debug`

### Audit Logging

#### `ZONE_GPT_AUDIT_LOG`
- **Description**: Path to the audit log file
- **Default**: `brain_audit.log` (in current working directory)
- **Example**: `ZONE_GPT_AUDIT_LOG=/var/log/zone-gpt/audit.log`
- **Note**: Ensure the directory exists and is writable

### Repository Configuration

#### `ZONE_GPT_REPO_PATH`
- **Description**: Path to the git repository root
- **Default**: Auto-detected (4 levels up from source files)
- **Example**: `ZONE_GPT_REPO_PATH=/opt/zone-gpt`
- **Note**: Only needed if auto-detection fails

## Configuration Examples

### Development Configuration

Create a `.env` file in the project root:

```bash
# Development settings
ZONE_GPT_HOST=127.0.0.1
ZONE_GPT_PORT=8000
ZONE_GPT_RELOAD=true
ZONE_GPT_LOG_LEVEL=debug

# Allow all origins for local development
ALLOWED_ORIGINS=*

# Local audit log
ZONE_GPT_AUDIT_LOG=./logs/audit.log
```

### Production Configuration

```bash
# Production settings
ZONE_GPT_HOST=0.0.0.0
ZONE_GPT_PORT=8000
ZONE_GPT_RELOAD=false
ZONE_GPT_LOG_LEVEL=warning

# Specific allowed origins
ALLOWED_ORIGINS=https://app.production.com,https://admin.production.com

# Centralized logging
ZONE_GPT_AUDIT_LOG=/var/log/zone-gpt/audit.log
ZONE_GPT_REPO_PATH=/opt/zone-gpt
```

### Docker Configuration

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install the application
COPY . .
RUN pip install .

# Set production environment variables
ENV ZONE_GPT_HOST=0.0.0.0
ENV ZONE_GPT_PORT=8000
ENV ZONE_GPT_RELOAD=false
ENV ZONE_GPT_LOG_LEVEL=info
ENV ZONE_GPT_AUDIT_LOG=/var/log/zone-gpt/audit.log

# Create log directory
RUN mkdir -p /var/log/zone-gpt

# Expose port
EXPOSE 8000

# Start the application
CMD ["zone-gpt"]
```

### Kubernetes Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: zone-gpt-config
data:
  ZONE_GPT_HOST: "0.0.0.0"
  ZONE_GPT_PORT: "8000"
  ZONE_GPT_RELOAD: "false"
  ZONE_GPT_LOG_LEVEL: "info"
  ALLOWED_ORIGINS: "https://app.example.com,https://admin.example.com"
  ZONE_GPT_AUDIT_LOG: "/var/log/zone-gpt/audit.log"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zone-gpt
spec:
  replicas: 3
  selector:
    matchLabels:
      app: zone-gpt
  template:
    metadata:
      labels:
        app: zone-gpt
    spec:
      containers:
      - name: zone-gpt
        image: zone-gpt:latest
        ports:
        - containerPort: 8000
        envFrom:
        - configMapRef:
            name: zone-gpt-config
        volumeMounts:
        - name: logs
          mountPath: /var/log/zone-gpt
      volumes:
      - name: logs
        emptyDir: {}
```

## Security Best Practices

### 1. CORS Configuration
- **Never use `ALLOWED_ORIGINS=*` in production**
- Always specify exact domains
- Include protocol (http/https) in origins
- Consider subdomains carefully

### 2. Network Binding
- Use `ZONE_GPT_HOST=127.0.0.1` for services behind a reverse proxy
- Use `0.0.0.0` only when necessary
- Always use a reverse proxy (nginx, traefik) in production

### 3. Logging
- Store audit logs in a secure, monitored location
- Implement log rotation
- Never log sensitive data
- Monitor audit logs for suspicious activity

### 4. Auto-Reload
- **NEVER** enable `ZONE_GPT_RELOAD=true` in production
- Use only for local development

## Loading Environment Variables

### From .env File

Install python-dotenv:
```bash
pip install python-dotenv
```

Load in your code:
```python
from dotenv import load_dotenv
load_dotenv()

# Now environment variables from .env are available
from zone_gpt import create_app
app = create_app()
```

### From Shell

```bash
export ZONE_GPT_PORT=8080
export ZONE_GPT_LOG_LEVEL=debug
zone-gpt
```

### From systemd Service

```ini
[Unit]
Description=ZONE-GPT Service
After=network.target

[Service]
Type=simple
User=zone-gpt
WorkingDirectory=/opt/zone-gpt
Environment="ZONE_GPT_HOST=0.0.0.0"
Environment="ZONE_GPT_PORT=8000"
Environment="ZONE_GPT_LOG_LEVEL=info"
Environment="ALLOWED_ORIGINS=https://app.example.com"
Environment="ZONE_GPT_AUDIT_LOG=/var/log/zone-gpt/audit.log"
ExecStart=/usr/local/bin/zone-gpt
Restart=always

[Install]
WantedBy=multi-user.target
```

## Troubleshooting

### Port Already in Use
Change the port:
```bash
ZONE_GPT_PORT=8080 zone-gpt
```

### Permission Denied on Log File
Ensure the log directory exists and is writable:
```bash
mkdir -p /var/log/zone-gpt
chmod 755 /var/log/zone-gpt
```

### CORS Errors in Browser
Check that your frontend origin is in `ALLOWED_ORIGINS`:
```bash
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080 zone-gpt
```

### Git Repository Not Found
Explicitly set the repository path:
```bash
ZONE_GPT_REPO_PATH=/path/to/repo zone-gpt
```

## Monitoring

### Health Check Endpoint

Create a simple health check:
```bash
curl http://localhost:8000/docs
```

### Audit Log Monitoring

Monitor the audit log in real-time:
```bash
tail -f /var/log/zone-gpt/audit.log
```

### Application Logs

Check uvicorn logs for application issues:
```bash
# With systemd
journalctl -u zone-gpt -f

# With Docker
docker logs -f zone-gpt-container
```
