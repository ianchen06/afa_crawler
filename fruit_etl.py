import datetime
import glob

import pandas as pd

fds = glob.glob('./fruit_data/*.html')
#fds = ['./data/2017-11-10T00:00:00+08:00.html', './data/2017-11-25T00:00:00+08:00.html', './data/2017-11-13T00:00:00+08:00.html', './data/2017-11-14T00:00:00+08:00.html', './data/2017-11-08T00:00:00+08:00.html', './data/2017-11-21T00:00:00+08:00.html', './data/2017-10-25T00:00:00+08:00.html', './data/2017-10-23T00:00:00+08:00.html', './data/2017-11-03T00:00:00+08:00.html', './data/2017-11-06T00:00:00+08:00.html', './data/2017-11-19T00:00:00+08:00.html', './data/2017-11-07T00:00:00+08:00.html', './data/2017-11-26T00:00:00+08:00.html', './data/2017-10-30T00:00:00+08:00.html', './data/2017-11-12T00:00:00+08:00.html', './data/2017-11-20T00:00:00+08:00.html', './data/2017-11-17T00:00:00+08:00.html', './data/2017-11-02T00:00:00+08:00.html', './data/2017-11-22T00:00:00+08:00.html', './data/2017-11-24T00:00:00+08:00.html', './data/2017-10-31T00:00:00+08:00.html', './data/2017-10-29T00:00:00+08:00.html', './data/2017-11-18T00:00:00+08:00.html', './data/2017-11-09T00:00:00+08:00.html', './data/2017-11-05T00:00:00+08:00.html', './data/2017-11-01T00:00:00+08:00.html', './data/2017-11-23T00:00:00+08:00.html', './data/2017-10-28T00:00:00+08:00.html', './data/2017-11-16T00:00:00+08:00.html', './data/2017-11-15T00:00:00+08:00.html', './data/2017-10-27T00:00:00+08:00.html', './data/2017-10-24T00:00:00+08:00.html', './data/2017-11-04T00:00:00+08:00.html', './data/2017-11-11T00:00:00+08:00.html', './data/2017-10-26T00:00:00+08:00.html']
for fd in fds:
    print('[INFO][%s]Doing %s'%(datetime.datetime.now().isoformat(), fd))
    with open(fd) as f:
        html = f.read()
        try:
            df = pd.read_html(html)[2]
            df.drop(df.index[:2], inplace=True)
            df['dt'] = fd.split('/')[-1].split('.html')[0]
            with open('./afa_fruit.csv', 'a') as f:
                df.to_csv(f, header=False)
        except ValueError:
            print('[ERROR] fd is %s'%fd)

