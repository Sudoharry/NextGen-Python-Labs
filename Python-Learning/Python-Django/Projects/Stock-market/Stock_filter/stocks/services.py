from nsetools import Nse
import pandas as pd
from datetime import datetime, timedelta
from .models import TopSector, Stock

class NseService:
    def __init__(self):
        self.nse = Nse()
        self.all_stocks = self.nse.get_stock_codes()
    
    def get_52w_high_low(self, symbol):
        quote = self.nse.get_quote(symbol)
        return {
            'high_52w': quote['high52'],
            'low_52w': quote['low52'],
            'current_price': quote['lastPrice']
        }
    
    def get_top_sectors(self, threshold=0.3):
        sectors = {}
        for symbol in self.all_stocks:
            if symbol == 'SYMBOL':
                continue  # Skip header
            try:
                data = self.get_52w_high_low(symbol)
                if (data['current_price'] >= data['high_52w'] * (1 - threshold)):
                    sector = self.nse.get_quote(symbol)['industry']
                    if sector not in sectors:
                        sectors[sector] = []
                    sectors[sector].append(symbol)
            except:
                continue
        
        # Rank sectors by number of qualifying stocks
        return sorted(sectors.items(), key=lambda x: len(x[1]), reverse=True)[:5]

    def update_stock_data(self):
        top_sectors = self.get_top_sectors()
        for sector, stocks in top_sectors:
            sector_obj, _ = TopSector.objects.update_or_create(
                name=sector,
                defaults={
                    'stocks_count': len(stocks),
                    'performance': self.calculate_sector_performance(sector)
                }
            )
            for symbol in stocks:
                data = self.get_52w_high_low(symbol)
                Stock.objects.update_or_create(
                    symbol=symbol,
                    defaults={
                        'name': self.all_stocks[symbol],
                        'sector': sector,
                        'current_price': data['current_price'],
                        'high_52w': data['high_52w'],
                        'low_52w': data['low_52w'],
                        'pe_ratio': self.nse.get_quote(symbol)['p'],
                        'market_cap': self.nse.get_quote(symbol)['marketCap']
                    }
                )

    def calculate_sector_performance(self, sector):
        # Implement sector performance calculation
        return 0.0  # Replace with actual calculation