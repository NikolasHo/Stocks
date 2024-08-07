DOMAIN = "Stocks"


def setup(hass, config):
    hass.states.set("Stocks.Value", "Rich")

    # Return boolean to indicate that initialization was successful.
    return True