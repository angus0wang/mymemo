ADD_MEMORY_TOOL = {
    "type": "function",
    "function": {
        "name": "add_memory",
        "description": "增加一条记忆",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "添加到记忆的数据"}
            },
            "required": ["data"],
            "additionalProperties": False
        },
    },
}

UPDATE_MEMORY_TOOL = {
    "type": "function",
    "function": {
        "name": "update_memory",
        "description": "更新记忆提供的ID和数据",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "memory_id": {
                    "type": "string",
                    "description": "要更新的记忆的memory_id",
                },
                "data": {
                    "type": "string",
                    "description": "记忆的更新数据",
                },
            },
            "required": ["memory_id", "data"],
            "additionalProperties": False
        },
    },
}

DELETE_MEMORY_TOOL = {
    "type": "function",
    "function": {
        "name": "delete_memory",
        "description": "按memory_id删除记忆",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "memory_id": {
                    "type": "string",
                    "description": "要删除的记忆的memory_id",
                }
            },
            "required": ["memory_id"],
            "additionalProperties": False
        },
    },
}
