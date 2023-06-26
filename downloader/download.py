import click

from datetime import date, datetime, timedelta
from download_data import download_data

@click.command()
@click.option('--tag', 'tag',
              prompt='Tag of the term',
              help='Tag of the term')
@click.option('--region', '-r', 'region',
              default=None,
              prompt='Geographic location of interest',
              prompt_required=False,
              help='Geographic location of interest')
@click.option('--start-date', 'start_date',
              prompt='Range start (YYYY-MM-DD)',
              help='Range start (YYYY-MM-DD)')
@click.option('--end-date', 'end_date',
              default=datetime.today().strftime('%Y-%m-%d'),
              help='Range end (YYYY-MM-DD)')
@click.option('--days', '-n',
              default=29,
              prompt='Number of days to request, >= 1',
              help='Number of days to requests')
@click.option('--proxy', '-p', 'proxy',
              default=False,
              prompt_required=False,
              help='Request proxies')
@click.option('--delay', '-d',
              default=10,
              help='Delay between request')
def add(tag, region, start_date, days, end_date, proxy, delay):
    start_date = date.fromisoformat(start_date)
    end_date = date.fromisoformat(end_date)
    if proxy == False:
        proxy = []

    directory = tag.replace('/', '.')

    current_date = end_date
    while current_date >= start_date:
        range_start = current_date
        range_end = current_date + timedelta(days=days)

        # Cap the data extraction
        if range_end >= end_date:
            print("Requested data outside boundary. Rescaled.")
            range_end = end_date

        download_data(directory=directory, tag=tag, region=region,
                      range_start=range_start, range_end=range_end,
                      days=days, proxies=proxy)
            
        # Tick forward one day
        current_date -= timedelta(days=1)

if __name__ == '__main__':
    add()