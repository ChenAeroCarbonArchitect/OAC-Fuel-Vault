"""
OAC-Fuel-Vault: Arbitrage & Risk Monitor
Essence: Real-time tracking of SAF spot prices vs. Vault collateral.
Author: ChenAeroCarbonArchitect
"""

class RiskMonitor:
    def __init__(self, maintenance_margin=1.2):
        # The collateral must be 1.2x the current market value
        self.maintenance_margin = maintenance_margin

    def check_health(self, order_id, current_market_price, collateral_amount, volume):
        """
        Check if the airline's deposit is still safe against market volatility.
        """
        current_value = current_market_price * volume
        health_factor = collateral_amount / current_value
        
        print(f"--- Monitoring {order_id} ---")
        print(f"Current Market Value: {current_value} USDC | Health Factor: {health_factor:.2f}")
        
        if health_factor < self.maintenance_margin:
            return "⚠️ MARGIN CALL: Request additional collateral or trigger liquidation."
        return "✅ Position Secure."

# Execution Logic
if __name__ == "__main__":
    monitor = RiskMonitor()
    
    # Simulate a scenario: 
    # Airline locked 1000 MT at $1000/MT (Collateral: 1.2M USDC)
    # But SAF price spikes to $1500/MT due to scarcity
    order_id = "ORDER-SAF-NESTE-2026"
    collateral = 1200000
    volume = 1000
    spot_price = 1500
    
    status = monitor.check_health(order_id, spot_price, collateral, volume)
    print(f"System Action: {status}")
