def analyze_file(file_path):
    data = {
        "file": file_path,
        "lines": 0,
        "functions": 0,
        "classes": 0,
        "comments": 0
    }

    try:
        with open(file_path,'r',encoding = "utf-8",errors = "ignore") as f:
            lines = f.readlines()
            data["lines"] = len(lines)

            for line in lines:
                line = line.strip()

                if line.startswith("def "):
                    data["functions"] += 1
                
                elif line.startswith("class"):
                    data["classes"] += 1
                elif line.startswith("#") or line.startswith("//") or line.startswith("/*") or line.startswith("*"):
                    data["comments"] += 1
                elif "(" in line and ")" in line and "{" in line and "}" in line: #c/java code
                    data["functions"] += 1   
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")

    return data
    