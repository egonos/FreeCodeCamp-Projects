def add_time(start, duration,day = None):
  sep_loc = start.find(":") 
  start_hour = int(start[:sep_loc])
  start_minutes = int(start[sep_loc+1: sep_loc+3])
  ampm = start[-2:]
  sep_loc2 = duration.find(":")
  dur_hour = int(duration[:sep_loc2])
  dur_minutes = int(duration[sep_loc2+1:])

  if ampm == "PM": start_hour += 12

  #calculations
  final_minutes = (dur_minutes + start_minutes)%60
  total_hours = start_hour + dur_hour + (start_minutes + dur_minutes) // 60
  final_hour = total_hours % 24
  days_later = total_hours // 24

  if final_hour == 0:
    final_hour = 12
  if final_hour > 12:
    final_hour -= 12
  if total_hours % 24 < 12:
    ampm = "AM"
  else:
    ampm = "PM"

  if day:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = (days.index(day.capitalize()) + days_later) % 7
    day = days[day_index]

  if days_later == 0:
    new_time = f'{final_hour}:{final_minutes:02d} {ampm}' + (f', {day}' if day else '')
  elif days_later == 1:
    new_time = f'{final_hour}:{final_minutes:02d} {ampm}, {day} (next day)' if day else f'{final_hour}:{final_minutes:02d} {ampm} (next day)'
  else:
    new_time = f'{final_hour}:{final_minutes:02d} {ampm}, {day} ({days_later} days later)' if day else f'{final_hour}:{final_minutes:02d} {ampm} ({days_later} days later)'

  return new_time
  
