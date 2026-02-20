# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Claude Code installer repository. It contains a single shell script (`claude_install.sh`) that downloads and installs Claude Code CLI.

## Usage

The installer can be run with an optional target parameter:
```bash
./claude_install.sh              # Install default version
./claude_install.sh stable       # Install stable version
./claude_install.sh latest       # Install latest version
./claude_install.sh 1.2.3        # Install specific version
```

## Architecture

The installer script:
1. Detects the platform (darwin/linux) and architecture (x64/arm64)
2. Handles Rosetta 2 detection on macOS (uses native arm64 binary when running under x64 emulation)
3. Detects musl libc on Linux and adjusts platform string accordingly
4. Downloads the binary from GCS bucket with SHA256 checksum verification
5. Runs the downloaded binary's `install` command to set up launcher and shell integration
6. Cleans up the downloaded file after installation

## Dependencies

- `curl` or `wget` (required)
- `jq` (optional, for JSON parsing; falls back to pure bash)
