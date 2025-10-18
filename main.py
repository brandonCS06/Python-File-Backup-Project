import json
import os
from backup import run_backup
from scheduler import start_schedule
def create_Config():
    from validate import validate_Path, validate_FileExtension

    print("Enter backup configuration:")
    source_dir = input("Enter the full path to the source folder: ").strip()
    backup_dir = input("Enter the full path to the backup destination folder: ").strip()
    #validate paths during configuration creation#
    try:
        source_dir = validate_Path(source_dir)
        backup_dir = validate_Path(backup_dir)
    except ValueError as e:
        print(f"Invalid path: {e}")
        return create_Config() #Retry config process#
    
    scheduleSet = input("Set automatic backup schedule (24 Hour Time): ").strip()
    maxBackups = int(input("Enter the max amount of backups: ").strip())
    config = {
        "source_dir": source_dir,
        "backup_dir": backup_dir,
        "include_extensions": [".txt",".jpg",".docx"],
        "max_backup_versions": maxBackups,
        "schedule": scheduleSet
    }

    with open("config.json","w") as f:
        json.dump(config,f,indent = 4)
    print("Config is saved to config.json")

    try:
        for ext in [".txt",".jpg",".docx"]:
            validate_FileExtension(ext)
    except ValueError as e:
        print(f"Invalid file extension: {e}")
        return create_Config() #Retry config process#
    return config

def load_Config():
    if not os.path.exists("config.json"):
        return create_Config()
    else:
        with open("config.json") as f:
            return json.load(f)

def main():
    config = load_Config()
    
    while True:
        print("\n Choose an option:")
        print("1. Run manual backup")
        print("2. Start scheduled backups")
        print("3. Change configuration")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            run_backup(config)
        elif choice == "2":
            start_schedule(config)
        elif choice == "3":
            config = create_Config()
        elif choice == "4":
            print("Exiting...")
            break
        else: 
            print("Invalid input. Please choose again (1/2/3)")
if __name__ == "__main__":
    main()