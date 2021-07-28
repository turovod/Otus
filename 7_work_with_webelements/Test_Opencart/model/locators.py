def get_by_btn_url(number_btn):
    return f'#content > div.row > div:nth-child({number_btn}) > div > div.button-group > ' \
           f'button:nth-child(1) > span'
