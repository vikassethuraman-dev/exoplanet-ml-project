import lightkurve as lk

def get_lightcurve(star_name):

    try:
        search_result = lk.search_lightcurve(
            star_name,
            mission="Kepler"
        )

        if len(search_result) == 0:
            print ("no data found for", star_name)
            return None

        lc = (
            search_result
            .download
            .remove_nans()
            .flatten()
        )

        return lc

    except Exception as e:
        print ("eror:", e)
        return None