def print_file_reports(data):
    print("\nPer-file report:")
    print("-"*30)

    for item in data:
        print(f"\nFile: {item.get('file', 'unknown')}")
        print(f"Lines: {item.get('lines', 0)}")
        print(f"Functions: {item.get('functions', 0)}")
        print(f"Classes: {item.get('classes', 0)}")
        print(f"Comments: {item.get('comments', 0)}")

        # ✅ PRINT WARNINGS
        warnings = item.get("warnings", [])
        for w in warnings:
            print(f"⚠️ {w}")

        print("-" * 30)
        
def print_worst_files(data):
    if not data:
        return

    largest_file = max(data, key=lambda x: x.get("lines", 0))
    most_functions = max(data, key=lambda x: x.get("functions", 0))
    most_classes = max(data, key=lambda x: x.get("classes", 0))

    print("\nWorst Files:")
    print("-"*30)

    print(f"Largest file: {largest_file.get('file')} ({largest_file.get('lines')} lines)")
    print(f"Most functions: {most_functions.get('file')} ({most_functions.get('functions')} functions)")
    print(f"Most classes: {most_classes.get('file')} ({most_classes.get('classes')} classes)")