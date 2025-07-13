#!/usr/bin/env python3
import os
import json
from datetime import datetime
import re

def extract_date_from_filename(filename):
    """Extract date from filename"""
    # Look for YYYYMMDD format
    date_match = re.search(r'(\d{8})', filename)
    if date_match:
        date_str = date_match.group(1)
        try:
            date_obj = datetime.strptime(date_str, '%Y%m%d')
            return date_obj.strftime('%Y-%m-%d')
        except:
            pass
    
    # Use file modification time
    return datetime.now().strftime('%Y-%m-%d')

def extract_title_from_filename(filename):
    """Extract title from filename"""
    # Remove .pdf extension
    title = filename.replace('.pdf', '')
    
    # Remove date part
    title = re.sub(r'\d{8}_?', '', title)
    
    # Convert underscores and hyphens to spaces
    title = title.replace('_', ' ').replace('-', ' ')
    
    # Convert multiple spaces to single space
    title = re.sub(r'\s+', ' ', title).strip()
    
    return title if title else filename.replace('.pdf', '')

def generate_pdf_list():
    """Generate file list from PDF directory"""
    pdf_dir = 'PDF'
    pdf_files = []
    
    if not os.path.exists(pdf_dir):
        print(f"Error: {pdf_dir} directory not found")
        return
    
    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith('.pdf'):
            title = extract_title_from_filename(filename)
            date = extract_date_from_filename(filename)
            
            pdf_info = {
                "title": title,
                "subtitle": "",  # Set manually as needed
                "filename": filename,
                "date": date
            }
            pdf_files.append(pdf_info)
    
    # Sort by date (newest first)
    pdf_files.sort(key=lambda x: x['date'], reverse=True)
    
    # Output as JavaScript file
    js_content = f"const pdfFiles = {json.dumps(pdf_files, ensure_ascii=False, indent=4)};"
    
    with open('pdf-files.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Generated pdf-files.js with {len(pdf_files)} files")
    for pdf in pdf_files:
        print(f"  - {pdf['title']} ({pdf['date']})")

if __name__ == "__main__":
    generate_pdf_list()