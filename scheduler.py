import schedule
import time
from backup import run_backup
from logger import get_logger

logger = get_logger()

def start_schedule(config):
    schedule_time = config.get("schedule","18:00")
    schedule.every().day.at(schedule_time).do(run_backup,config)

    logger.info(f"Scheduled daily backup at {schedule_time}")
    print("Schedule backups running. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        logger.info("Backup scheduler stopped by user")
    