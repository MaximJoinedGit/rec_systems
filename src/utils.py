def prefilter_items(data, item_features, take_n_popular=None):

    def popular(data):
    
        popularity = data.groupby('item_id')['user_id'].nunique().reset_index() 
        popularity['user_id'] = popularity['user_id'] / data['user_id'].nunique()
        popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
    
        return popularity
    
    popularity = popular(data)
    
    # Уберем самые популярные товары (их и так купят)
    top_popular = popularity[popularity['share_unique_users'] > 0.5].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]
    
    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.01].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]
    
    # Уберем товары, которые не продавались за последние 12 месяцев
    
    # Уберем не интересные для рекоммендаций категории (department)
    
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб. 
    
    # Уберем слишком дорогие товары
    
    # Возбмем n популярных товаров, если задан параметр take_n_popular.
    
    if take_n_popular:
        popularity = popular(data)
        top_n_popular = popularity.sort_values('share_unique_users')[:take_n_popular]['item_id'].tolist()
        data = data[data['item_id'].isin(top_n_popular)]
    
    return data
    
def postfilter_items(user_id, recommednations):
    pass