import re
import subprocess
from datetime import datetime
import os

def log_error(error_message):
    """Logs an error message with a timestamp to errors.log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {error_message}\n"
    with open("errors.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)
    print(f"An error occurred and was logged to errors.log.")

def write_report(original_file_name, results):
    """Writes the analysis results to report.txt."""
    try:
        with open("report.txt", "w", encoding="utf-8") as report_file:
            report_file.write(f"--- File Analysis Report for: {original_file_name} ---\n")
            for description, value in results.items():
                report_file.write(f"{description}: {value}\n")
        print(f"\nAnalysis report successfully written to report.txt.")
    except IOError as e:
        print(f"Failed to write report.txt: {e}")
        log_error(f"Failed to write report.txt: {e}")

def count_lines_efficient(file_name):
    """Counts the number of lines in a file"""
    with open(file_name, 'r', encoding='utf-8') as f:
        count = sum(1 for line in f)
    return count

def count_words_in_file(file_name):
    """Counts the total number of words in a file."""
    total_words = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split()
                total_words += len(words)
        return total_words
    except FileNotFoundError:
        log_error(f"FileNotFoundError in count_words_in_file for {file_name}")
        return 0

def count_chars_in_file(file_name):
    """Counts the total number of characters in a file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            return len(content)
    except Exception as e:
        log_error(f"Exception in count_chars_in_file for {file_name}: {e}")
        return 0

def count_empty_lines_compact(file_name):
    """Counts the number of empty lines or lines containing only whitespace."""
    with open(file_name, 'r', encoding='utf-8') as f:
        count = sum(1 for line in f if not line.strip())
    return count

file_name = None

while True:
    try:
        file_name = input("Enter file name: ")
        with open(file_name, 'r') as open_file:
            print(f"File '{file_name}' opened successfully for reading.")
        break  # Exit the loop if the file opens successfully

    except FileNotFoundError:
        print("Error: File not found. Please try again.")
        log_error(f"FileNotFoundError for input: {file_name}")
    
    except PermissionError:
        print("Access Error: Insufficient permissions to read the file. Please check permissions.")
        log_error(f"PermissionError for input: {file_name}")

    except IsADirectoryError:
        print("Error: The path specified is a directory, not a file. Please try again.")
        log_error(f"IsADirectoryError for input: {file_name}")

    except IOError as e:
        print(f"An unexpected I/O error occurred: {e}. Please try again.")
        log_error(f"IOError during file input validation for {file_name}: {e}")

if file_name:
    print(f"\nStarting analysis of '{file_name}'...")
    
    analysis_results = {
        "Lines Count": count_lines_efficient(file_name),
        "Words Count": count_words_in_file(file_name),
        "Characters Count": count_chars_in_file(file_name),
        "Empty Lines Count": count_empty_lines_compact(file_name)
    }
    
    for key, value in analysis_results.items():
        print(f"{key}: {value}")

    write_report(file_name, analysis_results)