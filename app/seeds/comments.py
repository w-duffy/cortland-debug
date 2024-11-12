from flask import current_app
from sqlalchemy.sql import text
from app.models import db, Comment, environment, SCHEMA
from datetime import datetime, timedelta


seed_project_data = [
    {
        "user_id": 1,
        "title": "Project Alpha",
        "description": "A project focused on developing Alpha software features.",
        "body": "This project will introduce essential features for alpha testing.",
        "goal": 5000.00,
        "amount": 1200.00,
        "location": "New York, NY",
        "media_url": "https://example.com/media/alpha.jpg",
        "deadline": datetime.now() + timedelta(days=30),
    },
    {
        "user_id": 2,
        "title": "Beta Testing Project",
        "description": "Testing the new features for beta users.",
        "body": "We will implement and test new features with selected beta users.",
        "goal": 1500.00,
        "amount": 600.00,
        "location": "San Francisco, CA",
        "media_url": "https://example.com/media/beta.jpg",
        "deadline": datetime.now() + timedelta(days=15),
    },
    {
        "user_id": 1,
        "title": "Data Analysis Platform",
        "description": "Creating a platform for advanced data analysis.",
        "body": "The platform will enable powerful data processing and visualization.",
        "goal": 10000.00,
        "amount": 2500.00,
        "location": "Chicago, IL",
        "media_url": "https://example.com/media/data-analysis.jpg",
        "deadline": datetime.now() + timedelta(days=45),
    },
]
def seed_comments():
    project1 = Comment(
        amount=seed_project_data[0]["amount"],
        user_id=seed_project_data[0]["user_id"],
        title=seed_project_data[0]["title"],
        description=seed_project_data[0]["description"],
        body=seed_project_data[0]["body"],
        goal=seed_project_data[0]["goal"],
        location=seed_project_data[0]["location"],
        media_url=seed_project_data[0]["media_url"],
        deadline=seed_project_data[0]["deadline"],
    )
    project2 = Comment(
        amount=seed_project_data[1]["amount"],
        user_id=seed_project_data[1]["user_id"],
        title=seed_project_data[1]["title"],
        description=seed_project_data[1]["description"],
        body=seed_project_data[1]["body"],
        goal=seed_project_data[1]["goal"],
        location=seed_project_data[1]["location"],
        media_url=seed_project_data[1]["media_url"],
        deadline=seed_project_data[1]["deadline"],
    )
    project3 = Comment(
        amount=seed_project_data[2]["amount"],
        user_id=seed_project_data[2]["user_id"],
        title=seed_project_data[2]["title"],
        description=seed_project_data[2]["description"],
        body=seed_project_data[2]["body"],
        goal=seed_project_data[2]["goal"],
        location=seed_project_data[2]["location"],
        media_url=seed_project_data[2]["media_url"],
        deadline=seed_project_data[2]["deadline"],
    )
    db.session.add(project1)
    db.session.add(project2)
    db.session.add(project3)
    db.session.commit()

def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
