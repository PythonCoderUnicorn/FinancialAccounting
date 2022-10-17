class Dupont_equation:
"""
    def __init__(self, dict_, list_) -> None:
        self.dict_ = dict_ 
        self.list_ = list_ 
    
    def profit_margin(self,dict_):
        assets_list = list(self.dict_.values())

        profit_margin = assets_list[0] / assets_list[1]
        answers.append(profit_margin)
        print("Profit margin = $ {:,.2f}".format(profit_margin))


    def avg_total_assets( self, dict_):
        assets_list = list(self.dict_.values())

        avg_tot_assets = (assets_list[2] + assets_list[3] ) / 2
        answers.append(avg_tot_assets)
        print("Average total assets = $ {:.2f}".format(avg_tot_assets))


    def asset_turnover( self, dict_, list_):
        assets_list = list(self.dict_.values())

        avg_tot_assets = (assets_list[2] + assets_list[3] ) / 2

        turnover = assets_list[1] / avg_tot_assets

        self.list_.append(turnover)
        
        print("The asset turnover = $ {:.2f}".format(turnover))


    def financial_leverage( self,dict_, list_ ):
        assets_list = list(self.dict_.values())

        fin_lev = assets_list[3] / assets_list[4]

        self.list_.append(fin_lev)
        print("Financial leverage = $ {:.2f}".format(fin_lev))


    def return_on_equity(self,answers):
        roe = answers[0] * answers[2] * answers[3]
        print("Return on equity = {:.2f}%".format(roe * 100))
        
        
        
        
pl = {
'net_income':185,
'net_sales':2628
}

bs = {
    'beginning_assets':5954,
    'ending_assets':4601,
    'ending_equity':1105,
}

roe = dupont_equation(pl,bs)
print(print_percentage(roe))


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
        return return_on_equity