def serialize_query_obj(obj):
    result = {}

    for k, v in obj.__dict__.items():
        if k != '_sa_instance_state':
            if hasattr(v, '__dict__'):
                result[k] = serialize_query_obj(v)
            else:
                result[k] = v

    return result

def serialize_query_list(lst):
    return [serialize_query_obj(item) for item in lst]