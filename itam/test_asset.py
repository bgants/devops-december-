from itam.Asset import Asset


def test_create_asset():
    laptop_asset = Asset(
        asset_id="A001",
        asset_type="Laptop",
        asset_name="Dell XPS 13",
        purchase_date="2023-01-01",
        purchase_cost=1200.00,
        vendor="Dell Inc.",
    )
    assert laptop_asset.asset_id == "A001"
    assert laptop_asset.asset_type == "Laptop"
    assert laptop_asset.asset_name == "Dell XPS 13"
    assert laptop_asset.purchase_date == "2023-01-01"
    assert laptop_asset.purchase_cost == 1200.00
    assert laptop_asset.vendor == "Dell Inc."
