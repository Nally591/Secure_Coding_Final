import argparse
import os
import re
import logging

SECRET_PATTERNS = {
    "Password": r'(?i)password\s*=\s*\S+',
    "AWS Access Key": r'AKIA[0-9A-Z]{16}',
    "GitHub Token": r'gh[pousr]_[A-Za-z0-9]{36,255}',
    "JWT Token": r'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+',
    "Private Key": r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'
}
logging.basicConfig(
    filename="scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser(
    description="Scan files or directories for possible hardcoded secrets."
)

parser.add_argument(
    "path",
    help="Path to the file or directory you want to scan"
)

args = parser.parse_args()
print("\nSecret Scanner Results")
print("-" * 50)
def scan_file(file_path):
    try:
        logging.info(f"Scanning file: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
        

                for secret_type, pattern in SECRET_PATTERNS.items():
                    matches = re.findall(pattern, line)

                    for match in matches:
                        logging.warning(
    f"Possible secret found in {file_path}, line {line_number}: {secret_type}"
)
                        print(
                            file_path,
                            "| Line:",
                            line_number,
                            "|",
                            secret_type,
                            "|",
                            match
                        )

    except Exception as e:
        logging.error(f"Could not read file {file_path}: {e}")
        print("Could not read file:", e)
if os.path.isfile(args.path):
    scan_file(args.path)

elif os.path.isdir(args.path):
    for root, folders, files in os.walk(args.path):
        for filename in files:
            file_path = os.path.join(root, filename)
            scan_file(file_path)

else:
    print("Error: Path does not exist.")