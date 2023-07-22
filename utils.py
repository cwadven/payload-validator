from datetime import datetime


def validate_date_parsing(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except (TypeError, ValueError):
        return False
