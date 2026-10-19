# Secure_Coding_Final

# Secret Scanner

## Overview

This project is a Python command-line tool that scans a file or directory for possible hardcoded secrets. It uses regular expressions to identify patterns that may contain sensitive information such as passwords, API keys, tokens, and private keys.

The purpose of the tool is to help identify credentials that may have accidentally been included in source code before the project is deployed or uploaded to a public repository.

## Secret Patterns

The scanner checks for the following patterns:

- Passwords
- AWS Access Keys
- GitHub Tokens
- JWT Tokens
- Private Keys

The matches are based on regular expression patterns. A match means that the text looks like a possible secret, but it does not guarantee that the credential is real or active.

## How It Works

The program accepts either a file path or directory path from the command line.

If a file is provided, the scanner reads the file line by line and checks each line against the secret patterns.

If a directory is provided, the program goes through the files in the directory and scans each one.

When a possible secret is found, the program displays:

- File name
- Line number
- Type of secret
- Matched string

The program also creates a `scanner.log` file that records the files that were scanned and any possible secrets that were detected.

## Usage

To scan a directory:

```bash
py secret_scanner.py test_files
