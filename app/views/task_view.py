def render_task_list(tasks):
    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
            "assigned_to": task.assigned_to,
        }
        for task in tasks
    ]


def render_task_detail(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "created_at": task.created_at,
        "assigned_to": task.assigned_to,
    }
