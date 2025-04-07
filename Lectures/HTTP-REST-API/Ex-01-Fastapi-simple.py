from fastapi import FastAPI, Query
from typing import List, Optional
import pandas as pd
import os 
import uvicorn


# Initialize FastAPI app
app = FastAPI()

# Sample data
data = pd.read_csv("medical_data.csv")

# Convert data to DataFrame
df = pd.DataFrame(data)

# Get SERVERNAME from environment variable
SERVERNAME = os.environ.get("SERVERNAME", "localhost")
# Get REPORT_URL from environment variable
REPORT_URL = os.environ.get("REPORT_URL", "")

@app.get(os.path.join("/", REPORT_URL, "health-check"))
def health_check():
    """Check whether the API is working."""
    return {"status": "API is working"}

@app.get(os.path.join("/", REPORT_URL, "columns"))
def get_columns():
    """Get usable column names."""
    return {"columns": df.columns.tolist()}

@app.get(os.path.join("/", REPORT_URL, "data"))
def get_data(
    year: int = Query(..., description="Year to filter data by"),
    gender: Optional[str] = Query(None, description="Gender to filter data by (male or female)"),
    columns: Optional[List[str]] = Query(None, description="Columns to include in the response")
):
    """Get data filtered by year, gender, and columns."""
    filtered_data = df[df["year"] == year]
    
    if gender:
        if gender.lower() not in ["male", "female"]:
            return {"error": "Invalid gender value. Please use 'male' or 'female'."}
        filtered_data = filtered_data[filtered_data["gender"].str.lower() == gender.lower()]
    
    if columns:
        # Validate requested columns
        invalid_columns = [col for col in columns if col not in df.columns]
        if invalid_columns:
            return {"error": f"Invalid columns requested: {invalid_columns}"}
        filtered_data = filtered_data[columns]
    
    return filtered_data.to_dict(orient="records")

@app.get(os.path.join("/", REPORT_URL))
def list_resources():
    """List all available resources and their descriptions."""
    return {
        "resources": {
            f"{SERVERNAME}/{REPORT_URL}health-check": {
                "description": "Check whether the API is working.",
                "example": f"{SERVERNAME}/{REPORT_URL}health-check"
            },
            f"{SERVERNAME}/{REPORT_URL}columns": {
                "description": "Get usable column names.",
                "example": f"{SERVERNAME}/{REPORT_URL}columns"
            },
            f"{SERVERNAME}/{REPORT_URL}data": {
                "description": "Get data filtered by year, gender, and columns.",
                "example": f"{SERVERNAME}/{REPORT_URL}data?year=2002&&columns=life_expectancy_male&columns=life_expectancy_female"
            }
        }
    }

REPORT_PORT = os.environ.get("REPORT_PORT", 9000)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=REPORT_PORT)
