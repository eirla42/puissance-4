from datetime import datetime


# Convert seconds into Hours:Minutes:Seconds
def seconds_to_h_m_s(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return "%02d:%02d:%02d" % (hours, minutes, seconds)


# Convert seconds into Datetime
def seconds_to_date(seconds):
    date = datetime.fromtimestamp(seconds)
    return date.strftime('%d-%m-%Y %H:%M:%S')
