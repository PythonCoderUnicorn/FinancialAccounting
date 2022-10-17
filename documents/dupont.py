class Dupont_equation:
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

 