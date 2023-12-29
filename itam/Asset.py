class Asset:
    def __init__(
        self,
        asset_id,
        asset_type,
        asset_name,
        purchase_date,
        purchase_cost,
        vendor,
        status="Active",
    ):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.asset_name = asset_name
        self.purchase_date = purchase_date
        self.purchase_cost = purchase_cost
        self.vendor = vendor
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def depreciate(self, depreciation_rate):
        # Perform depreciation calculations based on the depreciation rate
        # Update the asset value or other relevant attributes
        pass

    def __repr__(self):
        return (
            f"Asset(asset_id={self.asset_id}, "
            f"asset_type={self.asset_type}, "
            f"asset_name={self.asset_name}, "
            f"purchase_date={self.purchase_date}, "
            f"purchase_cost={self.purchase_cost}, "
            f"vendor={self.vendor}, "
            f"status={self.status})"
        )

    def display_info(self):
        print(f"Asset ID: {self.asset_id}")
        print(f"Asset Type: {self.asset_type}")
        print(f"Asset Name: {self.asset_name}")
        print(f"Purchase Date: {self.purchase_date}")
        print(f"Purchase Cost: ${self.purchase_cost}")
        print(f"Vendor: {self.vendor}")
        print(f"Status: {self.status}")
