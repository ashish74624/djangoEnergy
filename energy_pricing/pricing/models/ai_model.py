import numpy as np

class EnergyPricingModel:
    def __init__(self):
        self.base_price = 50  # Set base price to Rs. 50

    def predict_price(self, supply, demand, storage):
        # Simple dynamic formula for testing purposes:
        # Adjusts price based on relative differences
        price = self.base_price + (demand - supply) * 0.5 + storage * 0.1
        return round(price, 2)
