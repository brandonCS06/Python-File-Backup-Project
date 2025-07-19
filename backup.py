import os
import shutil
import datetime
import zipfile
from logger import get_logger

logger = get_logger()

def run_backup(config):
    source = config["source_dir"]
    dest = config["backup_dir"]
    extensions = tuple(config["include_extensions"])

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H5M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(dest, backup_name)

    logger.info("Starting backup...")

    with zipfile.ZipFile(backup_path,'w') as zipf:
        for foldername, subfolders, filenames in os.walk(source):
            for file in filenames:
                if file.endswith(extensions):
                    file_path = os.path.join(foldername,file)
                    arcname = os.path.relpath(file_path, source)
                    zipf.write(file_path,arcname)
                    logger.info(f"Backed up: {file_path}")
    logger.info(f"Backup completed: {backup_path}")
    clean_old_backups(dest, config["max_backup_versions"])
    print("Backup Completed!")

def clean_old_backups(backup_dir,max_versions):
    backups = sorted([
        f for f in os.listdir(backup_dir)
        if f.startswith("backup_") and f.endswith(".zip")
    ])

    if len(backups) > max_versions:
        for old_backup in backups[:-max_versions]:
            os.remove(os.path.join(backup_dir,old_backup))
            logger.info(f"Deleted old backup: {old_backup}")