from fastapi import HTTPException, status


def credentials_exception():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail=f"Could not validate credentials!",
                         headers={"WWW-Authenticate": "Bearer"})


def unauthorized():
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                         detail="Not authorized to perform requested action")


def not_found(content_name: str):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"{content_name} not found!")


def unprocessable_entity(err_msg: str):
    return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                         detail=err_msg)
