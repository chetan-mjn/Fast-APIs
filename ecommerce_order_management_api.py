from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Orders(BaseModel):
    order_id: int
    customer_name: str
    product_name: str
    quantity: int
    price_per_item: float
    status: str

statuses = ["pending", "shipped", "delivered"]

order_databases = []


@app.post("/orders")
def create_order(order: Orders):

    if order.quantity <= 0:
        return {
            "message": "Quantity must be greater than zero"
        }

    if order.status not in statuses:

        return{
            "message" : "invalid order status mentioned"
        }
    
    order_databases.append(order)

    return{
        "message" : "order placed successfully"
    }

@app.get("/orders/{order_id}/total")
def get_bill(order_id: int):

    for order in order_databases:

        if order.order_id == order_id:

            total_bill = order.quantity * order.price_per_item

            return{
                "order_id" : order.order_id,
                "customer_name" : order.customer_name,
                "total_bill" : total_bill
            }
    
    return{
        "message" : "order not found"
    }

@app.get("/orders/search")
def search_order_by_status(order_status: str):

    order_list = []

    for order in order_databases:

        if order.status.lower() == order_status.lower():

            order_list.append(order)

    return order_list

    

@app.get("/orders")
def get_orders():

    return order_databases

@app.get("/orders/{order_id}")
def get_one_order(order_id: int):

    for order in order_databases:

        if order.order_id == order_id:

            return order
        
    return{
        "message" : "invalid id entered"
    }

@app.put("/orders/{order_id}")
def update_order(order_id: int, new_order: Orders):

    if new_order.quantity <= 0:
        return {
            "message" : "Quantity must be greater than zero"
        }

    if new_order.status not in statuses:

        return{
            "message" : "Please select correct status"
        }

    for index, order in enumerate(order_databases):

        if order.order_id == order_id:

            order_databases[index] = new_order
            
            return{
                "message" : "order updated successfully"
            }
        
    return {
        "message" : "error updating order"
    }

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):

    for index, order in enumerate(order_databases):

        if order.order_id == order_id:

            order_databases.pop(index)
            return {
                "message" : "order deleted successfully"
            }
    return {
        "message" : "unable to delete order"
    }

