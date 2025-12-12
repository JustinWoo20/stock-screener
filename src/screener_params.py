from scraping.equity_field_params import *

regions = get_regions()
exchanges = get_exchanges()
sectors, industries = get_industries()
peer_groups = get_peer_groups()

screener_dictionary = {'Equity Fields': [{'Regions': regions,
                                   'Exchanges': exchanges,
                                   'Sectors': sectors,
                                   'Industries': industries,
                                   'Peer Groups': peer_groups,}],

                'Price': [{'eodprice': 'End of the day price',
                           'fiftytwowkpercentchange': '52 week percent change',
                           'intradaymarketcap': 'Intra day market cap',
                           'intradayprice': 'Intra day price',
                           'intradaypricechange': 'Intra day price change',
                           'lastclose52weekhigh.lasttwelvemonths': 'Previous 52 Week High',
                           'lastclose52weeklow.lasttwelvemonths': 'Previous 52 Week Low',
                           'lastclosemarketcap.lasttwelvemonths': 'Market Cap',
                           'percentchange': 'percent change',
                           }],

                'Trading': [{'avgdailyvol3m': 'Average 3 month daily volume',
                             'beta': 'Beta',
                             'dayvolume': 'Day volume',
                             'eodvolume': 'End of day volume',
                             'pctheldinsider': 'Percent held by insiders',
                             'pctheldinst': 'Percent held by institutions',}],

                'Short Interest': [{'days_to_cover_short.value': 'Days to Cover',
                                  'short_interest.value': 'Short Interest',
                                  'short_interest_percentage_change.value': 'Change in Short Interest',
                                  'short_percentage_of_float.value': 'Short Percentage of Float',
                                  'short_percentage_of_shares_outstanding.value': 'Short Percentage of Shares Outstanding',
                                  }],

                'Valuation': [{'bookvalueshare.lasttwelvemonths': 'TTM BVPS',
                               'lastclosemarketcaptotalrevenue.lasttwelvemonths': 'Market cap to total revenue',
                               'lastclosepriceearnings.lasttwelvemonths': 'TTM P/E',
                               'lastclosepricetangiblebookvalue.lasttwelvemonths': 'TTM P/TBV',
                               'lastclosetevtotalrevenue.lasttwelvemonths': 'Enterprise Value to Sales ratio',
                               'pegratio_5y': '5 year PEG ratio',
                               'pricebookratio.quarterly': 'P/B ratio', }],

                'Profitability': [{'consecutive_years_of_dividend_growth_count': 'Consecutive years of dividend growth',
                                   'forward_dividend_per_share': 'Projected yearly dividend',
                                   'forward_dividend_yield': 'Projected yearly dividend yield',
                                   'returnonassets.lasttwelvemonths': 'TTM ROA',
                                   'returnonequity.lasttwelvemonths': 'TTM ROE',
                                   'returnontotalcapital.lasttwelvemonths': 'TTM ROTC', }],

                'Leverage': [{'ebitdainterestexpense.lasttwelvemonths': 'Interest coverage (EBITDA-based)',
                              'ebitinterestexpense.lasttwelvemonths': 'Interest coverage (EBIT-based)',
                              'ltdebtequity.lasttwelvemonths': 'Long term debt to equity',
                              'totaldebtequity.lasttwelvemonths': 'Total debt to equity',
                              }],

                'Liquidity': [{'altmanzscoreusingtheaveragestockinformationforaperiod.lasttwelvemonths': 'Altman Z-Score',
                                'currentratio.lasttwelvemonths': 'TTM Current Ratio',
                                'operatingcashflowtocurrentliabilities.lasttwelvemonths': 'OCF Ratio',
                                'quickrtatio.lasttwelvemonths': '12 month quick ratio',
                               }],

                'Income Statement': [{'basicepscontinuingoperations.lasttwelvemonths': 'TTM EPS',
                                     'dilutedeps1yrgrowth.lasttwelvemonths': 'TTM Diluted EPS',
                                     'ebit.lasttwelvemonths': 'TTM EBIT',
                                     'ebitda.lasttwelvemonths': 'TTM EBITDA',
                                     'ebitda1yrgrowth.lasttwelvemonths': '1 Year EBITDA Growth',
                                     'ebitdamargin.lasttwelvemonths': 'TTM EBITDA Margin',
                                     'epsgrowth.lasttwelvemonths': '1 Year EPS Growth',
                                     'grossprofit.lasttwelvemonths': 'TTM Gross Profit',
                                     'grossprofitmargin.lasttwelvemonths': 'TTM Gross Profit Margin',
                                     'netincome1yrgrowth.lasttwelvemonths': '1 Year Net Income Growth',
                                     'netincomeis.lasttwelvemonths': 'TTM Net Income',
                                     'netincomemargin.lasttwelvemonths': 'TTM Net Income Margin',
                                     'operatingincome.lasttwelvemonths': 'TTM Operating Income',
                                     'quarterlyrevenuegrowth.quarterly': 'Quarterly Revenue Growth',
                                     'totalrevenues.lasttwelvemonths': 'TTM Total Revenues',
                                     'totalrevenues1yrgrowth.lasttwelvemonths': '1 Year Revenue Growth',
                                      }],

                'Balance Sheet': [{'totalassets.lasttwelvemonths': 'Total Assets',
                                    'totalcashandshortterminvestments.lasttwelvemonths': ' TTM Total Cash and Short Term Investments',
                                    'totalcommonequity.lasttwelvemonths': 'Last Reported Common Equity',
                                    'totalcommonsharesoutstanding.lasttwelvemonths': 'Outstanding shares (not diluted)',
                                    'totalcurrentassets.lasttwelvemonths': 'Current Assets',
                                    'totalcurrentliabilities.lasttwelvemonths': 'Current Liabilities',
                                    'totaldebt.lasttwelvemonths': 'Total Debt',
                                    'totalequity.lasttwelvemonths': 'Total Equity',
                                    'totalsharesoutstanding': 'Outstanding Shares (diluted)',}],
                'Cash Flow': [{'capitalexpenditure.lasttwelvemonths': 'Capital Expenditure',
                                'cashfromoperations.lasttwelvemonths': 'Cash from Operations',
                                'cashfromoperations1yrgrowth.lasttwelvemonths': '1 Year Cash from Operations Growth',
                                'leveredfreecashflow.lasttwelvemonths': 'LFCF',
                                'leveredfreecashflow1yrgrowth.lasttwelvemonths': '1 Year LFCF Growth',
                                'unleveredfreecashflow.lasttwelvemonths': 'UFCF',}],
                'ESG': [{'environmental_score': 'Environmental Score',
                        'esg_score': 'ESG Score',
                        'governance_score': 'Governance Score',
                        'highest_controversy': 'Highest Controversy',
                        'social_score': 'Social Score',}],
                }

# for item in screener_dictionary.keys():
#     print(item)


# price_metrics = {'Price': [{'eodprice': 'End of the day price',
#                             'fiftytwowkpercentchange': '52 week percent change',
#                             'intradaymarketcap': 'Intra day market cap',
#                             'intradayprice': 'Intra day price',
#                             'intradaypricechange': 'Intra day price change',
#                             'lastclose52weekhigh.lasttwelvemonths': 'Previous 52 Week High',
#                             'lastclose52weeklow.lasttwelvemonths': 'Previous 52 Week Low',
#                             'lastclosemarketcap.lasttwelvemonths': 'Market Cap',
#                             'percentchange': 'percent change',}]}

# trading_metrics = {'Trading': [{'avgdailyvol3m': 'Average 3 month daily volume',
#                                 'beta': 'Beta',
#                                 'dayvolume': 'Day volume',
#                                 'eodvolume': 'End of day volume',
#                                 'pctheldinsider': 'Percent held by insiders',
#                                 'pctheldinst': 'Percent held by institutions',}]}

# short_interest_metrics = {'Short Interest': [{'days_to_cover_short.value': 'Days to Cover',
#                                               'short_interest.value': 'Short Interest',
#                                               'short_interest_percentage_change.value': 'Change in Short Interest',
#                                               'short_percentage_of_float.value': 'Short Percentage of Float',
#                                               'short_percentage_of_shares_outstanding.value': 'Short Percentage of Shares Outstanding',
#                                               }]}

# valuation_metrics = {'Valuation': [{'bookvalueshare.lasttwelvemonths': 'TTM BVPS',
#                                     'lastclosemarketcaptotalrevenue.lasttwelvemonths': 'Market cap to total revenue',
#                                     'lastclosepriceearnings.lasttwelvemonths': 'TTM P/E',
#                                     'lastclosepricetangiblebookvalue.lasttwelvemonths': 'TTM P/TBV',
#                                     'lastclosetevtotalrevenue.lasttwelvemonths': 'Enterprise Value to Sales ratio',
#                                     'pegratio_5y': '5 year PEG ratio',
#                                      'pricebookratio.quarterly': 'P/B ratio',}]}

# profitability_metrics = {'Profitability': [{'consecutive_years_of_dividend_growth_count': 'Consecutive years of dividend growth',
#                                             'forward_dividend_per_share': 'Projected yearly dividend',
#                                             'forward_dividend_yield': 'Projected yearly dividend yield',
#                                             'returnonassets.lasttwelvemonths': 'TTM ROA',
#                                             'returnonequity.lasttwelvemonths': 'TTM ROE',
#                                             'returnontotalcapital.lasttwelvemonths': 'TTM ROTC',}]}

# leverage_metrics = {'Leverage': [{'ebitdainterestexpense.lasttwelvemonths': 'Interest coverage (EBITDA-based)',
#                                 'ebitinterestexpense.lasttwelvemonths': 'Interest coverage (EBIT-based)',
#                                   'ltdebtequity.lasttwelvemonths': 'Long term debt to equity',
#                                   'totaldebtequity.lasttwelvemonths': 'Total debt to equity',
#                                   }]}

# liquidity_metrics = {'Liquidity': [{'altmanzscoreusingtheaveragestockinformationforaperiod.lasttwelvemonths': 'Altman Z-Score',
#                                     'currentratio.lasttwelvemonths': 'TTM Current Ratio',
#                                     'operatingcashflowtocurrentliabilities.lasttwelvemonths': 'OCF Ratio',
#                                     'quickrtatio.lasttwelvemonths': '12 month quick ratio',}]}

# income_statement_metrics = {'Income Statement':[{'basicepscontinuingoperations.lasttwelvemonths': 'TTM EPS',
#                                                  'dilutedeps1yrgrowth.lasttwelvemonths': 'TTM Diluted EPS',
#                                                  'ebit.lasttwelvemonths': 'TTM EBIT',
#                                                  'ebitda.lasttwelvemonths': 'TTM EBITDA',
#                                                  'ebitda1yrgrowth.lasttwelvemonths': '1 Year EBITDA Growth',
#                                                  'ebitdamargin.lasttwelvemonths': 'TTM EBITDA Margin',
#                                                  'epsgrowth.lasttwelvemonths': '1 Year EPS Growth',
#                                                  'grossprofit.lasttwelvemonths': 'TTM Gross Profit',
#                                                  'grossprofitmargin.lasttwelvemonths': 'TTM Gross Profit Margin',
#                                                  'netincome1yrgrowth.lasttwelvemonths': '1 Year Net Income Growth',
#                                                  'netincomeis.lasttwelvemonths': 'TTM Net Income',
#                                                  'netincomemargin.lasttwelvemonths': 'TTM Net Income Margin',
#                                                  'operatingincome.lasttwelvemonths': 'TTM Operating Income',
#                                                  'quarterlyrevenuegrowth.quarterly': 'Quarterly Revenue Growth',
#                                                  'totalrevenues.lasttwelvemonths': 'TTM Total Revenues',
#                                                  'totalrevenues1yrgrowth.lasttwelvemonths': '1 Year Revenue Growth',
#                                                  }]}
#
# balance_sheet_metrics = {'Balance Sheet': [{'totalassets.lasttwelvemonths': 'Total Assets',
#                                             'totalcashandshortterminvestments.lasttwelvemonths': ' TTM Total Cash and Short Term Investments',
#                                             'totalcommonequity.lasttwelvemonths': 'Last Reported Common Equity',
#                                             'totalcommonsharesoutstanding.lasttwelvemonths': 'Outstanding shares (not diluted)',
#                                             'totalcurrentassets.lasttwelvemonths': 'Current Assets',
#                                             'totalcurrentliabilities.lasttwelvemonths': 'Current Liabilities',
#                                             'totaldebt.lasttwelvemonths': 'Total Debt',
#                                             'totalequity.lasttwelvemonths': 'Total Equity',
#                                             'totalsharesoutstanding': 'Outstanding Shares (diluted)',}]}
#
# cash_flow_metrics = {'Cash Flow': [{'capitalexpenditure.lasttwelvemonths': 'Capital Expenditure',
#                                     'cashfromoperations.lasttwelvemonths': 'Cash from Operations',
#                                     'cashfromoperations1yrgrowth.lasttwelvemonths': '1 Year Cash from Operations Growth',
#                                     'leveredfreecashflow.lasttwelvemonths': 'LFCF',
#                                     'leveredfreecashflow1yrgrowth.lasttwelvemonths': '1 Year LFCF Growth',
#                                     'unleveredfreecashflow.lasttwelvemonths': 'UFCF',}]}

# esg_metrics = {'ESG': [{'environmental_score': 'Environmental Score',
#                         'esg_score': 'ESG Score',
#                         'governance_score': 'Governance Score',
#                         'highest_controversy': 'Highest Controversy',
#                         'social_score': 'Social Score',}]}

