import pandas as pd
import pdb

# returns a sorted dataframe of size (#shops x #items x #days, 6)
# with columns (shop_id, item_id, item_price, day, date_block_num, item_cnt_day)
def fill_all(train):
    d = pd.date_range('1/1/2013', '10/12/2015')


def fill_dates(x, start, end, block_map):
    d = pd.date_range(start, end)
    t = x.reindex(d).drop('date',axis=1)
    t = t.reset_index().rename({'index': 'date'},axis=1)
    return fill_nan(t, block_map)

def fill_nan(t, block_map):
    t.loc[:,'shop_id'] = t['shop_id'].fillna(method='ffill').fillna(method='bfill')
    t['item_id'] = t['item_id'].fillna(method='ffill').fillna(method='bfill')
    t['item_price'] = t['item_price'].fillna(method='ffill').fillna(method='bfill')
    t['item_cnt_day'] = t['item_cnt_day'].fillna(0)
    t['date_block_num'] = t['date'].apply(block_map)
    return t

if __name__ == "__main__":
    train = pd.read_csv('../sales_train.csv.gz')
    fill_all(train)