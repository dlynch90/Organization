# Use the official Visual Studio Code Universal Container as base
FROM mcr.microsoft.com/vscode/devcontainers/universal:2

# Install Python dependencies
RUN python -m pip install --upgrade pip && 
    pip install uv && 
    uv venv .venv && 
    source .venv/bin/activate && 
    uv sync

# Set working directory
WORKDIR /Users/daniellynch/Desktop/Organization

# Expose ports if needed
EXPOSE 8080

# Command to run when container starts
CMD ["code", "."]