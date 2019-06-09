# "Most existing PV system programs assume PV module soiling loss that is constant through time. Our observations of measured performance suggest that performance losses due to system soiling are not constant through time, rather they depend on the amount and frequency of rain that falls on the system"
soiling_rate = float(.2)

def get_cleaning_threshold(rainfall):
    if rainfall < .2:
        loss = 0
    elif .4 > rainfall .2:
