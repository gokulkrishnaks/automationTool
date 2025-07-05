from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from datetime import datetime, timedelta
import random

app = FastAPI(title="Content Automation System", version="1.0.0")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create mock_data directory if it doesn't exist
os.makedirs("mock_data", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Initialize mock data files
def initialize_mock_data():
    # Trending topics data
    trends_data = {
        "trends": [
            {
                "id": 1,
                "topic": "AI in Healthcare",
                "score": 95,
                "category": "Technology",
                "growth_rate": "+23%",
                "volume": 45000,
                "timestamp": "2024-07-05T10:00:00Z"
            },
            {
                "id": 2,
                "topic": "Sustainable Fashion",
                "score": 87,
                "category": "Lifestyle",
                "growth_rate": "+18%",
                "volume": 32000,
                "timestamp": "2024-07-05T09:30:00Z"
            },
            {
                "id": 3,
                "topic": "Remote Work Tools",
                "score": 82,
                "category": "Business",
                "growth_rate": "+15%",
                "volume": 28000,
                "timestamp": "2024-07-05T09:00:00Z"
            },
            {
                "id": 4,
                "topic": "Plant-Based Nutrition",
                "score": 78,
                "category": "Health",
                "growth_rate": "+12%",
                "volume": 25000,
                "timestamp": "2024-07-05T08:30:00Z"
            },
            {
                "id": 5,
                "topic": "Cryptocurrency Updates",
                "score": 75,
                "category": "Finance",
                "growth_rate": "+10%",
                "volume": 38000,
                "timestamp": "2024-07-05T08:00:00Z"
            }
        ]
    }
    
    # AI-generated content data
    content_data = {
        "content": [
            {
                "id": 1,
                "title": "How AI is Revolutionizing Patient Care in 2024",
                "description": "Explore the latest AI applications transforming healthcare delivery and patient outcomes.",
                "content_type": "blog_post",
                "status": "pending",
                "trend_id": 1,
                "generated_at": "2024-07-05T10:15:00Z",
                "word_count": 850,
                "readability_score": 8.2,
                "seo_score": 92,
                "target_audience": "Healthcare professionals"
            },
            {
                "id": 2,
                "title": "10 Sustainable Fashion Brands Leading the Change",
                "description": "Discover eco-friendly fashion brands making a positive impact on the environment.",
                "content_type": "listicle",
                "status": "approved",
                "trend_id": 2,
                "generated_at": "2024-07-05T09:45:00Z",
                "word_count": 1200,
                "readability_score": 7.8,
                "seo_score": 88,
                "target_audience": "Fashion enthusiasts"
            },
            {
                "id": 3,
                "title": "The Future of Remote Work: Tools and Trends",
                "description": "Essential tools and emerging trends shaping the remote work landscape.",
                "content_type": "guide",
                "status": "pending",
                "trend_id": 3,
                "generated_at": "2024-07-05T09:15:00Z",
                "word_count": 950,
                "readability_score": 8.5,
                "seo_score": 90,
                "target_audience": "Business professionals"
            },
            {
                "id": 4,
                "title": "Plant-Based Nutrition: Complete Beginner's Guide",
                "description": "Everything you need to know about starting a plant-based diet.",
                "content_type": "guide",
                "status": "rejected",
                "trend_id": 4,
                "generated_at": "2024-07-05T08:45:00Z",
                "word_count": 1100,
                "readability_score": 7.5,
                "seo_score": 85,
                "target_audience": "Health-conscious consumers"
            },
            {
                "id": 5,
                "title": "Crypto Market Analysis: July 2024 Update",
                "description": "Latest cryptocurrency trends and market predictions for investors.",
                "content_type": "analysis",
                "status": "approved",
                "trend_id": 5,
                "generated_at": "2024-07-05T08:15:00Z",
                "word_count": 800,
                "readability_score": 8.0,
                "seo_score": 87,
                "target_audience": "Crypto investors"
            }
        ]
    }
    
    # Performance analytics data
    performance_data = {
        "analytics": [
            {
                "content_id": 2,
                "title": "10 Sustainable Fashion Brands Leading the Change",
                "published_date": "2024-07-03T10:00:00Z",
                "views": 15420,
                "engagement_rate": 7.8,
                "shares": 342,
                "comments": 89,
                "likes": 1203,
                "click_through_rate": 4.2,
                "bounce_rate": 32.5,
                "time_on_page": 185,
                "conversion_rate": 2.1
            },
            {
                "content_id": 5,
                "title": "Crypto Market Analysis: July 2024 Update",
                "published_date": "2024-07-02T14:30:00Z",
                "views": 23150,
                "engagement_rate": 9.2,
                "shares": 567,
                "comments": 134,
                "likes": 2031,
                "click_through_rate": 5.8,
                "bounce_rate": 28.3,
                "time_on_page": 220,
                "conversion_rate": 3.4
            },
            {
                "content_id": 1,
                "title": "How AI is Revolutionizing Patient Care in 2024",
                "published_date": "2024-07-01T09:15:00Z",
                "views": 18750,
                "engagement_rate": 8.5,
                "shares": 445,
                "comments": 112,
                "likes": 1592,
                "click_through_rate": 4.9,
                "bounce_rate": 30.1,
                "time_on_page": 195,
                "conversion_rate": 2.8
            }
        ],
        "summary": {
            "total_content_published": 12,
            "total_views": 187420,
            "average_engagement_rate": 8.2,
            "total_shares": 2341,
            "total_comments": 567,
            "average_conversion_rate": 2.8
        }
    }
    
    # Write mock data to JSON files
    with open("mock_data/trends.json", "w") as f:
        json.dump(trends_data, f, indent=2)
    
    with open("mock_data/content.json", "w") as f:
        json.dump(content_data, f, indent=2)
    
    with open("mock_data/performance.json", "w") as f:
        json.dump(performance_data, f, indent=2)

# Initialize mock data on startup
initialize_mock_data()

# Helper function to load JSON data
def load_json_data(filename):
    try:
        with open(f"mock_data/{filename}", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Data file {filename} not found")

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Content Automation System API", "version": "1.0.0"}

@app.get("/trends")
async def get_trends():
    """Get trending topics data"""
    data = load_json_data("trends.json")
    return data

@app.get("/content")
async def get_content():
    """Get AI-generated content ideas"""
    data = load_json_data("content.json")
    return data

@app.get("/performance")
async def get_performance():
    """Get post-performance analytics"""
    data = load_json_data("performance.json")
    return data

@app.post("/content/{content_id}/approve")
async def approve_content(content_id: int):
    """Simulate content approval"""
    # Mock approval logic
    return {
        "message": f"Content {content_id} approved successfully",
        "content_id": content_id,
        "status": "approved",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/content/{content_id}/reject")
async def reject_content(content_id: int):
    """Simulate content rejection"""
    # Mock rejection logic
    return {
        "message": f"Content {content_id} rejected",
        "content_id": content_id,
        "status": "rejected",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/dashboard/stats")
async def get_dashboard_stats():
    """Get dashboard statistics"""
    return {
        "total_trends": 5,
        "pending_content": 2,
        "approved_content": 2,
        "rejected_content": 1,
        "total_views": 187420,
        "avg_engagement": 8.2,
        "conversion_rate": 2.8
    }

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/dashboard")
async def serve_dashboard():
    """Serve the main dashboard HTML file"""
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)