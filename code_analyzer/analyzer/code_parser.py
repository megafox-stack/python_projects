from utils.helpers import read_file, count_lines, clean_line

def analyze_file(file_path):
    data = {
        "file": file_path,
        "lines": 0,
        "functions": 0,
        "classes": 0,
        "comments": 0,
        "warnings": []
    }

    lines = read_file(file_path)
    data["lines"] = count_lines(lines)

    for line in lines:
        line = clean_line(line)

    
        if (line.startswith("//") or 
            line.startswith("#") or 
            line.startswith("/*") or 
            line.startswith("*")):
            data["comments"] += 1

        if line.startswith("def "):
            data["functions"] += 1

        elif ("(" in line and ")" in line and 
              "{" in line and not line.startswith("//")):
            data["functions"] += 1


        elif line.startswith("class "):
            data["classes"] += 1


    if data["lines"] > 300:
        data["warnings"].append("file too large")
    
    if data["functions"] > 5:            
        data["warnings"].append("too many functions")
    if data["classes"] > 5:
        data["warnings"].append("too many classes")    
 
    return data
    