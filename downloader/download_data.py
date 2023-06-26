from pytrends.request import TrendReq

from os import remove, mkdir
from os.path import exists, join

"""
Singleton Initiation
"""
pytrend = TrendReq(
    hl='en-US', tz=0,
    backoff_factor=5,
)  # Start request session

def download_data(directory, tag, region, range_start, range_end, days, proxies):
    if proxies == []:
        global pytrend
    else:
        pytrend = TrendReq(
            hl='en-US', tz=0,
            backoff_factor=0.5,
            proxy=proxies
        )
    filename = join(directory, range_start)

    if not exists(directory):
        mkdir(directory) 

    if exists(filename):
        print(f"[w] {filename} already exist. Skipping...")
        return
    else:
        print(f"[w] Downloading {filename}...")
        pytrend.build_payload(kw_list=[tag],
                            cat=0,
                            timeframe=f"{range_start} {range_end}",
                            geo=region)
        df = pytrend.interest_over_time()

        if(len(df) < days):
            print(f"[w] [{filename}] is incompleted. Saving as partial")
            filename += ".partial"
        else:
            partial_filename = f"{filename}.partial.csv"
            
            if exists(partial_filename):
                remove(partial_filename)
        
        filename += ".csv"
        df.to_csv(filename)