kwargs = {}
for key in keys:
    try:
        kwargs[key] = input_dict[key]
    except KeyError:
        pass

return kwargs

def soiling_kimber(self,rainfall_timeseries, soiling_rate_daily=0.0015, grace_period=14,
                   rain_threshold=30, locale='rural', scheduled_cleaning_dates=None):
 """
    Parameters
    ----------
    rainfall_timeseries : pandas.DataFrame
        a timeseries of rainfall in millimeters
    threshold : float, default 6[mm]
        the amount of rain in millimeters [mm] required to clean the panels
    soiling_rate: float, default 0.15%
        daily soiling rate, enter as fraction, not percent
    grace_period: int, default 14-days
        The time after a rainfall event when it's assumed the ground is damp, and
        so it's assumed there is no soiling. Change to smaller value for dry climate
    max_soiling: float, default 30%
        maximum soiling, soiling will accumulate until this value
    manual_wash_dates: sequence or None, default None
        A list or tuple of dates when the panels were manually cleaned. Note there
        is no grace period after a manual cleaning, so soiling begins to accumulate
        immediately after a manual cleaning, sorry :(

    Returns
    -------
    soiling : timeseries
        the daily soiling
    """
    import pandas as pd
    import datetime

    # manual wash dates
    if manual_wash_dates is None:
        manual_wash_dates = []

    # resample rainfall as days by summing intermediate times
    rainfall = pd.resample(rainfall_timeseries, freq="D").sum()

    # soiling
    soiling = np.zeros_like(rainfall)

    # rainfall events that clean the panels
    rain_events = rainfall > rain_threshold

    # loop over days
    for today in rainfall.index:

        # did rain exceed threshold?
        rain_exceed_thresh = rainfall[today] > rain_threshold

        # if yes, then set soiling to zero
        if rain_exceed_thresh:
            soiling[today] = 0
            continue

        # start day of grace period
        start_day = today - grace_period

        # rainfall event during grace period?
        rain_in_grace_period = any( rain_events [ start_day : today ] )

        # if rain exceeded threshold during grace period,
        # assume ground is still damp, so no or v. low soiling
        if rain_in_grace_period:
            soiling[today] = 0
            continue

        # is this a manual wash date?
        if today in manual_wash_dates:
            soiling[today] = 0
            continue

        # so, it didn't rain enough to clean, it hasn't rained enough recently,
        # and we didn't manually clean panels, so soil them by adding daily
        # soiling rate to soiling from previous day
        total_soil = soiling[today - datetime.timedelta(days=1)] + soiling_rate

        # check if soiling has reached the maximum
        soiling[today] = max_soiling if (total_soil >= max_soiling) else total_soil


kwargs = _build_kwargs(['rainfall_timeseries','locale','scheduled_cleaning_dates'], self.module_parameters)
    return soiling_kimber(soiling_rate_daily,rain_threshold,grace_period,**kwargs)
