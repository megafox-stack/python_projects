from analyzer.file_scanner import scan_files
from analyzer.code_parser import analyze_file
from analyzer.stats import print_file_reports
from analyzer.stats import print_worst_files

def main():
    path = input("enter the path to analyze: ").strip()

    files = scan_files(path)

    results = []
    for file in files:
        result = analyze_file(file)
        results.append(result)

    print_file_reports(results)
    print_worst_files(results)
    

if __name__ == "__main__":
    main()