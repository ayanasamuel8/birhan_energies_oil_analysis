"""
Modeling Module for the Birhan Energies project.

This module contains functions for building, running, and analyzing the
Bayesian changepoint models used to detect structural breaks in Brent
oil price volatility.
"""

import pandas as pd
import numpy as np
import pymc as pm
from typing import Union

def run_volatility_changepoint_model(
    log_returns_data: Union[pd.Series, np.ndarray],
    draws: int = 2000,
    tune: int = 3000,
    cores: int = 4
) -> pm.backends.base.MultiTrace:
    """
    Defines and runs a Bayesian changepoint model to detect a single
    shift in the volatility of a time series.

    The model assumes the time series (log returns) has a mean of zero and
    switches from one volatility level (sigma_1) to another (sigma_2) at an
    unknown point in time (tau).

    Args:
        log_returns_data (Union[pd.Series, np.ndarray]): A series or array of
            daily log returns to be modeled.
        draws (int): The number of samples to draw from the posterior.
        tune (int): The number of tuning (burn-in) steps.
        cores (int): The number of CPU cores to use for sampling.

    Returns:
        pm.backends.base.MultiTrace: The trace object containing the results
                                     of the MCMC sampling.
    """
    if not isinstance(log_returns_data, (pd.Series, np.ndarray)):
        raise TypeError("Input data must be a pandas Series or numpy ndarray.")

    n_days = len(log_returns_data)
    print(f"--- Building Bayesian model for {n_days} data points ---")

    with pm.Model() as volatility_model:
        # Prior for the switch point (tau). It can be any day from the second to the last.
        tau = pm.DiscreteUniform("tau", lower=1, upper=n_days - 1)

        # Priors for the "before" and "after" volatilities (standard deviations).
        # Exponential is a good choice for scale parameters like standard deviation.
        sigma_1 = pm.Exponential("sigma_1", 1.0)
        sigma_2 = pm.Exponential("sigma_2", 1.0)

        # Create an index for the days
        day_idx = np.arange(n_days)

        # Use pm.math.switch to select the correct volatility for each day.
        # If the day index is less than tau, use sigma_1; otherwise, use sigma_2.
        current_sigma = pm.math.switch(tau > day_idx, sigma_1, sigma_2)

        # Likelihood of the data.
        # We model the log returns as a Normal distribution with a mean of 0
        # and a standard deviation (sigma) that changes at the switch point.
        returns = pm.Normal(
            "returns",
            mu=0,
            sigma=current_sigma,
            observed=log_returns_data
        )

        # Run the MCMC sampler to find the posterior distributions of the parameters.
        print(f"\nRunning MCMC sampler (draws={draws}, tune={tune}, cores={cores})...")
        try:
            trace = pm.sample(draws=draws, tune=tune, cores=cores, progressbar=True)
            print("--- MCMC Sampling Complete ---")
            return trace
        except Exception as e:
            print(f"An error occurred during MCMC sampling: {e}")
            return None