def calculate_stats(data):
    total_files = len(data)
    total_lines = sum(item["lines"] for item in data)
    total_functions = sum(item["functions"] for item in data)
    total_classes = sum(item["classes"] for item in data)
    total_comments = sum(item["comments"] for item in data)

    return {
        "total_files": total_files,
        "total_lines": total_lines,
        "total_functions": total_functions,
        "total_classes": total_classes,
        "total_comments": total_comments
    }

def print_stats(stats):
    print(f"Total Files: {stats['total_files']}")
    print(f"Total Lines: {stats['total_lines']}")
    print(f"Total Functions: {stats['total_functions']}")
    print(f"Total Classes: {stats['total_classes']}")
    print(f"Total Comments: {stats['total_comments']}")