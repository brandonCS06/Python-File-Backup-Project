import os
import shutil
import datetime
import zipfile
from logger import get_logger
last_BackupFile = "last_backup.txt"
logger = get_logger()

def run_backup(config):
    source = config["source_dir"]
    dest = config["backup_dir"]
    extensions = tuple(config["include_extensions"])
    from validate import validate_Path, validate_FileExtension
    #Validating process#
    try:
        source = validate_Path(config["source_dir"])
        dest = validate_Path(config["backup_dir"])

        #validate extensions#
        for ext in extensions:
            validate_FileExtension(ext)
        logger.info("Path and extensions validation passed")
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"Error: {e}")
        return
    extensions = tuple(config["include_extensions"])
    
    # Load last backup timestamp
    if os.path.exists(last_BackupFile):
            with open(last_BackupFile, "r") as f:
                last_backup_str = f.read().strip()
                try:
                    last_backup_time = datetime.datetime.fromisoformat(last_backup_str)
                except ValueError:
                    last_backup_time = None
    else:
            last_backup_time = None
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(dest, backup_name)

    logger.info("Starting backup...")

    
    files_for_backup = []
    for foldername, subfolders, filenames in os.walk(source):
        for file in filenames:
            if file.endswith(extensions):
                file_path = os.path.join(foldername,file)
                if last_backup_time:
                    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    logger.info(f"Checking file: {file_path} | Modified: {modified_time} | Last backup: {last_backup_time}")
                    #check if file has been modified since last backup#
                    if last_backup_time and modified_time <= last_backup_time + datetime.timedelta(seconds = 1):
                        logger.info(f"Skipped unchanged file: {file_path}")
                        continue
                    arcname = os.path.relpath(file_path, source)
                    files_for_backup.append((file_path, arcname))
    if not files_for_backup:
        logger.info("No files changed since last backup")
        print("No changes detected. Backup skipped")
        return
    with zipfile.ZipFile(backup_path,'w') as zipf:
         for file_path, arcname in files_for_backup:
              zipf.write(file_path, arcname)
              logger.info(f"Backed up: {file_path}")
    logger.info(f"Backup completed: {backup_path}")
    #encryption process#
    if config.get("encryption",True):
        from encrypt import generate_Key, encrypt_File
        import json

        #load or generate encryption key#
        key_file = config.get("encryption_key","backup_key.key")
        if os.path.exists(key_file):
            with open(key_file,'rb') as f:
                key = f.read()
        else:
            key = generate_Key()
            with open(key_file,'wb') as f:
                f.write(key)
        encrypted_Path = encrypt_File(backup_path,key)
        logger.info(f"Encrypted backup: {encrypted_Path}")
    
    clean_old_backups(dest, config["max_backup_versions"])
    with open(last_BackupFile,"w") as f:
         f.write(datetime.datetime.now().isoformat())
    print("Backup Completed!")

def clean_old_backups(backup_dir,max_versions):
    backups = sorted([
        f for f in os.listdir(backup_dir)
        if f.startswith("backup_") and (f.endswith(".zip") or f.endswith(".zip.enc"))
    ])

    if len(backups) > max_versions:
        for old_backup in backups[:-max_versions]:
            os.remove(os.path.join(backup_dir,old_backup))
            logger.info(f"Deleted old backup: {old_backup}")