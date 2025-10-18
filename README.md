# Python File Backup Tool
A Python tool that can provide manual and automatic file backup capabilities with encryption, logging, and file change detection
---
## Features
- **Manual & Automatic Backups**: Run backups on-demand or schedule them automatically
- **Smart Change Detection**: Only backs up files that have been modified since the last backup
- **File Type Support**: Configurable file extensions (default: .txt, .jpg, .docx)
- **Compression**: Creates compressed .zip archives for efficient storage
- **Encryption**: Optional AES encryption for secure backup storage
- **Comprehensive Logging**: Detailed activity logs with timestamps
- **Backup Management**: Automatic cleanup of old backups based on version limits
- **Configuration Management**: Easy setup and modification via JSON configuration
- **Path Validation**: Built-in validation for source and destination paths

## Requirements
- Python 3.7 or higher
- [`schedule`](https://pypi.org/project/schedule/) - For automatic backup scheduling
- [`cryptography`](https://pypi.org/project/cryptography/) - For encryption functionality

---
## Setup Instructions
1. Clone Repository
```bash
git clone https://github.com/brandonCS06/python-file-backup.git
cd python-file-backup
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run the Program
```bash
python main.py
```
## How It Works
On first run, you'll be prompted to configure:
* **Source Folder** - Directory containing files to back up
* **Backup Destination** - Where backup archives will be stored
* **Schedule Time** - When to run automatic backups (24-hour format)
* **Max Backup Versions** - How many backup versions to keep

After configuration, choose from the main menu:
1. **Run manual backup** - Execute an immediate backup
2. **Start scheduled backups** - Begin automatic scheduled backups
3. **Change configuration** - Modify settings
4. **Exit** - Close the application

### Smart Backup Features
- **Change Detection**: Only files modified since the last backup are included
- **Incremental Backups**: Saves time and storage by skipping unchanged files
- **Automatic Cleanup**: Removes old backups beyond the version limit
- **Encryption**: Optional AES encryption for sensitive data protection

## Configuration
The JSON configuration file (`config.json`) is automatically created on first run and contains:

```json
{
  "source_dir": "/Users/yourname/Documents/source",
  "backup_dir": "/Users/yourname/Documents/backups",
  "include_extensions": [".txt", ".jpg", ".docx"],
  "max_backup_versions": 5,
  "schedule": "18:00",
  "encryption": true,
  "encryption_key": "backup_key.key"
}
```

### Configuration Options
- **`source_dir`**: Path to the directory containing files to back up
- **`backup_dir`**: Destination directory for backup archives
- **`include_extensions`**: List of file extensions to include in backups
- **`max_backup_versions`**: Maximum number of backup versions to keep
- **`schedule`**: Time for automatic backups (24-hour format, e.g., "18:00")
- **`encryption`**: Enable/disable backup encryption (default: true)
- **`encryption_key`**: Filename for the encryption key (auto-generated if not exists)

## File Structure
```
python-file-backup/
├── main.py              # Main application entry point
├── backup.py            # Core backup functionality
├── encrypt.py           # Encryption/decryption utilities
├── scheduler.py         # Automatic backup scheduling
├── validate.py          # Path and file validation
├── logger.py            # Logging configuration
├── utils.py             # Utility functions
├── config.json          # Configuration file (auto-generated)
├── requirements.txt     # Python dependencies
├── last_backup.txt      # Last backup timestamp
└── logs/
    └── backup.log       # Application logs
```

## Logging
All backup activities are logged to `logs/backup.log` with timestamps, including:
- Backup start/completion
- Files processed and skipped
- Error messages and validation failures
- Old backup cleanup activities
