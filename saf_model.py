"""
OAC-Fuel-Vault: Core SAF Asset Modeling
Essence: Transforming physical fuel futures into verifiable digital assets.
Project: OAC-Fuel-Vault (Sustainable Aviation Fuel Liquidity Protocol)
"""

import hashlib
import time

class SAFBatch:
    """
    Represents a specific batch of Sustainable Aviation Fuel.
    Each batch is a unique asset with distinct carbon credentials.
    """
    def __init__(self, supplier, volume_mt, carbon_intensity_reduction, delivery_window):
        # The entity producing the SAF (e.g., 'Neste', 'SkyNRG')
        self.supplier = supplier
        # Volume in Metric Tons
        self.volume_mt = volume_mt
        # Life-cycle carbon reduction (e.g., 0.80 = 80% reduction vs Fossil Jet A1)
        self.carbon_intensity_reduction = carbon_intensity_reduction
        # Delivery Window (e.g., '2026-Q4')
        self.delivery_window = delivery_window
        # Digital Identity of the batch
        self.asset_id = self._generate_asset_id()
        # Status: Pending | Verified | Delivered
        self.status = "Pending"

    def _generate_asset_id(self):
        """
        Creates a unique hash for the fuel batch to ensure traceability.
        """
        raw_data = f"{self.supplier}-{self.volume_mt}-{self.delivery_window}-{time.time()}"
        return hashlib.sha256(raw_data.encode()).hexdigest()[:12]

    def get_asset_summary(self):
        """
        Returns a clean summary of the SAF asset.
        """
        return {
            "ID": self.asset_id,
            "Producer": self.supplier,
            "Volume": f"{self.volume_mt} MT",
            "Carbon_Reduction": f"{self.carbon_intensity_reduction * 100}%",
            "Timeline": self.delivery_window,
            "Verification_Status": self.status
        }

# Execution context for validation
if __name__ == "__main__":
    # Simulate the creation of a high-value SAF asset
    batch_001 = SAFBatch(
        supplier="Neste_Refinery_01", 
        volume_mt=1000, 
        carbon_intensity_reduction=0.85, 
        delivery_window="2026-Dec"
    )
    
    print("--- OAC Fuel Vault: Asset Tokenization ---")
    summary = batch_001.get_asset_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
