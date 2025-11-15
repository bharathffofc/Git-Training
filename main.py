import uvicorn
from fastapi import FastAPI
from route import router,auth_router

app=FastAPI(title="Simple Note Manager",description="A Mini Project using Fastapi and MongoDB.",docs_url="/mini")
app.include_router(router)
app.include_router(auth_router)

# if __name__ == '__main__':
#     uvicorn.run(app,host="127.0.0.1",port=8000)

result = response.json()
assert response.status_code == 403
assert result["detail"] == [
    {
        "error_details": "Login Error",
        "loc": ["login", "is_token_expired"],
        "msg": "invalid token",
        "title": "LOGIN ERROR",
        "type": "validation_studio_error.semantic",
    }
]