from indeed import extract_indeed_pages, extract_indeed_jobs

max_indeed_pages = extract_indeed_pages()

extracted_jobs=extract_indeed_jobs(max_indeed_pages)

print(extracted_jobs)