def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{hours:02}:{minutes:02}:{sec:02}"

total_seconds = int(input("Enter total seconds of video: "))
print("Converted Time:", convert_seconds(total_seconds))
