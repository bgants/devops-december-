# Example Usage:
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List
import uvicorn
from itam.Asset import Asset


app = FastAPI()


class AssetCreateIn(BaseModel):
    asset_id: str
    asset_type: str
    asset_name: str
    purchase_date: str
    purchase_cost: float
    vendor: str
    status: str = "Active"


class AssetOut(BaseModel):
    asset_id: str
    asset_type: str
    asset_name: str
    purchase_date: str
    purchase_cost: float
    vendor: str
    status: str = "Active"


assets = []


@app.get("/assets", response_model=List[AssetOut])
def read_assets():
    return assets


@app.get("/assets/{asset_id}", response_model=AssetOut)
def read_asset(asset_id: str):
    for asset in assets:
        if asset.asset_id == asset_id:
            return asset
    raise HTTPException(status_code=404, detail="Asset not found")


@app.post("/assets")
def create_asset(asset: AssetCreateIn = Body(...)):
    asset_model = Asset(**asset.dict())
    assets.append(asset_model)
    return {"message": "Asset created successfully"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
