"""
OAC-Fuel-Vault: Liquidity & Escrow Engine
Essence: Managing airline deposits and risk collateralization for SAF futures.
Author: ChenAeroCarbonArchitect
"""

class FuelVault:
    def __init__(self, protocol_fee_rate=0.005):
        # The percentage of each transaction that goes into your pocket (0.5%)
        self.protocol_fee_rate = protocol_fee_rate
        self.total_locked_value = 0.0
        self.active_orders = {}
        self.accumulated_fees = 0.0

    def place_preorder(self, airline_name, saf_batch, deposit_amount):
        """
        Airlines deposit stablecoins to lock in a specific SAF batch.
        @param deposit_amount: Funds sent by the airline (USDC/USDT)
        """
        # Calculate protocol's cut immediately (Wealth Maximization)
        fee = deposit_amount * self.protocol_fee_rate
        net_deposit = deposit_amount - fee
        self.accumulated_fees += fee
        
        order_id = f"ORDER-{saf_batch.asset_id}"
        self.active_orders[order_id] = {
            "client": airline_name,
            "asset_id": saf_batch.asset_id,
            "collateral": net_deposit,
            "status": "Locked"
        }
        
        self.total_locked_value += net_deposit
        print(f"--- Order Placed: {order_id} ---")
        print(f"Airline: {airline_name} | Net Deposit: {net_deposit} USDC | Protocol Revenue: {fee} USDC")
        return order_id

# Simulation for the "Aero-Wealth" logic
if __name__ == "__main__":
    from saf_model import SAFBatch
    
    # 1. Initialize the Vault with 0.5% fee
    vault = FuelVault(protocol_fee_rate=0.005)
    
    # 2. Create a batch of future SAF (from our previous model)
    future_oil = SAFBatch("SkyNRG_Amsterdam", 2000, 0.90, "2026-Nov")
    
    # 3. An airline (e.g., Cathay Pacific) locks 1,000,000 USDC
    vault.place_preorder("Cathay_Pacific", future_oil, 1000000)
    
    print(f"\nTotal Protocol Revenue Earned: {vault.accumulated_fees} USDC")
    print(f"Total Value Locked (TVL) in Protocol: {vault.total_locked_value} USDC")
