# Data Annotation Engineer Project

## Overview

This project involved extracting information from invoices using an API, applying regular expressions (regex) for data extraction, and utilizing Python to automate the process. The goal was to efficiently process and extract relevant details from five invoices provided.

## Project Requirements

**API Usage:** Utilize a provided API to fetch data related to the invoices.

**Regex Application:** Extract key pieces of information (such as invoice number, date, total amount, etc.) from the API response using regular expressions.

**Python Programming:** Implement the logic using Python to handle the extraction process and ensure accuracy.

## Approach

**1. Fetching Data:**

The first step was to connect to the provided API and retrieve the data corresponding to each invoice. The API response was in a structured format (e.g., JSON), which contained the invoice details.

**2. Data Extraction:**

I applied regular expressions to extract specific information from the raw API response. This included:
* vendor name
* vendor address
* bill to name
* invoice number
* date
* Line items

**3. Data Validation:**

Once the relevant information was extracted, I validated it against the structure and context of the invoices to ensure its accuracy.

**4. Automation:**

The entire process was automated using Python script. This included fetching data from the API, applying regex, and storing the extracted information in a structured format (e.g., JSON).

## Technologies Used

* **Python:** The core programming language used to implement the solution.
* **Regular Expressions (Regex):** Utilized for pattern matching and extracting specific data from the API response.
* **API:** Interfaced with the provided API(Veryfi API) to retrieve invoice data.

## Code Structure

**1. API Interaction:**

A function that connects to the API, retrieves data, and handles any necessary authentication or headers.

**2. Regex Extraction:**

A set of functions that apply regular expressions to the API response to extract relevant details (invoice number, date, total amount, etc.).

**3. Data Processing:**

A function that processes the extracted data, ensuring it is in the correct format for further use (e.g., saving to JSON).
