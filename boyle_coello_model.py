
def boyle_coello_model(self,time,rain = 0,rainthreshold = 0,tilt = 0,pm2_5 = 0,pm_10=,**kwargs):

    """
    Use the :py:func:`boyle_coello_model` function to determine the impact of dirt accumulation on performance.

    Parameters
    ----------
    time : numeric
        Importing the datetime module would be suitable here
    rain : array-like
        Hourly rain accumulation values of the same duration defined in the time parameter. Units in milimeters.
    rainthreshold : float
        A scalar for the amount of rain in an accumulation period needed to clear the modules. In periods where the accumulated rain meets oro exceeds the threshold, the panels are assumed to be cleaned immediately after the accumulation period.
    tilt : int
        A scalar or vector for the tilt of the PV panels.
    PM2_5 : float
        The concentration of particulate matter with diamter less than 2.5 microns, in g/m^3.
    PM10 : float
        The concentration of particulate matter with diamter less than 10 microns, in g/m^3.
    ModelType : int
        Optional input to determine the model type to be used in the soiling model. A value of "1"

    RainAccPeriod :
        optional input that specifies the period, in hours
        over which to accumulate rainfall totals before checking against the
        rain cleaning threshold.

    Returns
    -------
    See pvsystem.calcparams_cec for details
    """



    kwargs = _build_kwargs([''])
