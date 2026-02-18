"""
Stub router with /api prefix. All future chat endpoints will be registered here
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api")  # All routes here will be prefixed with /api

# API endpoints will be added here in the next steps