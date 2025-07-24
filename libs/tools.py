from datetime import datetime
import logging


async def seconds_count(lg: logging.Logger, time_start: datetime, text: str):
    time_end = datetime.now()
    diff = time_end - time_start
    lg.info(f"{text}. Прошло: {diff.total_seconds()} сек.")


