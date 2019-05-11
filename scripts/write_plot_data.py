import pandas as pd

def write_data_to_plot(
    series, filename, sample_rate='300S', lower_quantile=.01, upper_quantile=0.99
):
    data = pd.DataFrame(series.resample(sample_rate).median().dropna().round(1))
    data = data[(data > data.quantile(lower_quantile)) & (data < data.quantile(upper_quantile))] # remove outliers
    data.columns = ['data_col']
    data.to_csv('plots/data/{}.csv'.format(filename), index_label='datetime')

if __name__ == '__main__':
    input_dir = 'data/'
    # temperature
    input_filename = '{}/{}'.format(input_dir, 'hot.csv')
    hot = pd.read_csv(
        input_filename, index_col='datetime', parse_dates=True
    ).resample('60S').mean().dropna()
    hot['temperature_f'] = hot['temperature_c']*(9.0/5.0) + 32
    write_data_to_plot(hot['temperature_f'], filename='hot')
