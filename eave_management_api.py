from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

leave_requests = []

class LeaveRequest(BaseModel):
    emp_id: int
    emp_name: str
    days: int
    reason: str

@app.post("/leave_request")
def add_leave(emp: LeaveRequest):

    leave_requests.append(emp)

    return {
        "message" : "leave request submitted"
    }

@app.get("/leave_request")
def get_leave_requests():

    return leave_requests

@app.get("/leave_request/{emp_id}")
def get_emp_leave_req(emp_id: int):

    for emp in leave_requests:

        if emp.emp_id == emp_id:

            return emp
    return{
        "message" : "no emp found with leave request"
    }

@app.delete("/leave_request/{emo_id}")
def delete_request(emp_id: int):

    for index, emp in enumerate(leave_requests):

        if emp.emp_id == emp_id:

            leave_requests.pop(index)

            return{
                "message" : "leave req deleted successfully ",
                "emp" : emp
            }
    
    return {
        "message" : "no emp found with request"
    }

@app.put("/leave_request/{emp_id}")
def update_leave(emp_id: int, new_leave: LeaveRequest):

    for index, emp in enumerate (leave_requests):

        if emp.emp_id == emp_id:

            leave_requests[index] = new_leave

            return{
                "message" : "leave updated"
            }

    return {
        "message" : "no emp founded"
    }
