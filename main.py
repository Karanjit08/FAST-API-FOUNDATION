from fastapi import FastAPI, HTTPException, Query
from models import MenuResponse, MenuItem
from data import menu_items
from typing import Optional


app = FastAPI(
    title= "CHAI POINT MENU API"
)


@app.get("/")
def root():
    return {"message": "Welcome to Chai Point Menu"}

@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: Optional[str] = Query(
        default=None,
        description="Filter menu by category"
    )
):
    try:
        # Get all available categories from the data
        valid_categories = {
            item["category"].lower()
            for item in menu_items
        }
        # Return all items if no category is provided
        if category is None:
            return MenuResponse(
                status="success",
                count=len(menu_items),
                items=menu_items,
            )
        category = category.lower().strip()
        # Validate category
        if category not in valid_categories:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": f"'{category}' is not a valid category.",
                    "allowed_categories": sorted(valid_categories),
                },
            )

        # Filter items
        filtered_items = [
            item
            for item in menu_items
            if item["category"].lower() == category
        ]

        return MenuResponse(
            status="success",
            count=len(filtered_items),
            items=filtered_items,
        )
    
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}",
        )

    
@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    try:
        # Find the menu item by id
        menu_item = next(
            (item for item in menu_items if item["id"] == id),
            None
        )

        if menu_item is None:
            raise HTTPException(
                status_code=404,
                detail=f"Menu item with id {id} not found."
            )

        return menu_item

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )