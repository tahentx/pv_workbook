
def boyle_coello_model(self,time,rain = 0,rainthreshold = 0,tilt = 0,pm2_5 = 0,pm_10=,**kwargs):

    """
    Use the :py:func:`boyle_coello_model` function to determine the impact of dirt accumulation on performance.

    Parameters
    ----------
    time : numeric
        Importing the datetime module would be suitable here

    rain : array-like
        Hourly rain accumulation values of the same duration defined in the time parameter. Units in milimeters.


    Returns
    -------
    See pvsystem.calcparams_cec for details
    """



    kwargs = _build_kwargs([''])
