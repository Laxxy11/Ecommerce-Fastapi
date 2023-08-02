async def success_response(status_code, data_info, msg=None):
    data_obj = {
        "details": {
            "status": True,
            "status_code": status_code,
            "msg": msg,
            "data": data_info,
        }
    }
    return data_obj
