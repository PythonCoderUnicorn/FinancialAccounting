class Dupont_equation:
    
"""      
profit_loss = {
'net_income':185,
'net_sales':2628
}

balance_sheet = {
    'beginning_assets':5954,
    'ending_assets':4601,
    'ending_equity':1105,
}

"""
    def make_profit_margin(net_income,net_sales):
        profit_margin = net_income/net_sales
        return profit_margin

    def make_average_total_assets(beginning_assets, ending_assets):
        average_total_assets = (beginning_assets + ending_assets)/2
        return average_total_assets

    def make_asset_turnover(net_sales, average_total_assets):
        asset_turnover = net_sales/average_total_assets
        return asset_turnover

    def make_financial_leverage(ending_assets,ending_equity):
        financial_leverage = ending_assets/ending_equity
        return financial_leverage

    def make_return_on_equity(profit_margin, asset_turnover, financial_leverage):
        return_on_equity = profit_margin * asset_turnover * financial_leverage
        return return_on_equity

    def print_percentage(float_num):
        percentage_number = float_num*100
        decimal_index = str(percentage_number).find(".")
        percent_return = f'{percentage_number:{decimal_index}.1f}%'
        return percent_return

    def dupont_equation(pl,bs):
        profit_margin = make_profit_margin(pl['net_income'], pl['net_sales'])
        average_total_assets = make_average_total_assets(bs['beginning_assets'], bs['ending_assets'])
        asset_turnover = make_asset_turnover(pl['net_sales'], average_total_assets)
        financial_leverage = make_financial_leverage(bs['ending_assets'], bs['ending_equity'])
        return_on_equity = make_return_on_equity(profit_margin, asset_turnover, financial_leverage)
        # return return_on_equity