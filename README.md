# Python File Backup Tool
A tool made in Python that can manually or automatically back up files from one folder to another.
---
## Features
- Manual backups on user demand
- Backs up file types: ".txt", ".jpg", and ".docx"
- Compresses backups into a ".zip" file
- Logs all backup activity
- Configurable settings via JSON file

## Requirements
- Python 3.7 or higher
- [`schedule`](https://pypi.org/project/schedule/) (install with pip)

---
## Setup Instructions
1. Clone Repository
```bash
git clone https://github.com/brandonCS06/python-file-backup.git
cd python-file-backup
```
2. Install Dependencies
```bash
pip install schedule
```
3. Run the Program
```bash
python main.py
```
## How It Works
On first run, you'll be prompted to set:
* Source Folder - Folder you want to back up
* Backup folder - Where backups are stored
Then, choose:
1. Run a manual backup
2. Start scheduled backups
3. Change configuration
4. Exit
Only the latest backups are kept based on your "max_backup_versions" setting

## Configuration
The JSON configuration file is structured as:
```
{
  "source_dir": "/Users/yourname/Documents/source",
  "backup_dir": "/Users/yourname/Documents/backups",
  "include_extensions": [".txt", ".pdf", ".jpg"],
  "max_backup_versions": 5,
  "schedule": "18:00"
}
```
* schedule is in 24-hour format
