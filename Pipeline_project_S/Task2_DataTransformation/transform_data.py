import json
import csv
import sys

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Successfully loaded {len(data)} records from {file_path}")
            return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {file_path} - {e}")
        sys.exit(1)

def filter_customers(data, threshold):
    """Filter customers with purchases above the threshold."""
    filtered = []
    for customer in data:
        try:
            if "Customer ID" not in customer or "Name" not in customer or "Total Purchases" not in customer:
                raise KeyError(f"Missing required keys in record: {customer}")
            if not isinstance(customer["Total Purchases"], (int, float)):
                raise ValueError(f"Invalid Total Purchases value: {customer['Total Purchases']} in record {customer}")
            
            if customer["Total Purchases"] > threshold:
                filtered.append(customer)
        except (KeyError, ValueError) as e:
            print(f"Warning: Skipping invalid record - {e}")
    print(f"Filtered {len(filtered)} customers with purchases > {threshold}")
    return filtered

def save_to_csv(data, output_file):
    """Save filtered data to a CSV file."""
    try:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Customer ID", "Name", "Total Purchases"])
            for customer in data:
                writer.writerow([customer["Customer ID"], customer["Name"], round(customer["Total Purchases"], 2)])
        print(f"Summary report saved to {output_file}")
    except Exception as e:
        print(f"Error: Could not save to {output_file} - {e}")
        sys.exit(1)

def main():
    # Default values
    input_file = "customer_data.json"
    output_file = "filtered_customers.csv"
    threshold = 500

    # Dynamic parameters from command-line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    if len(sys.argv) > 3:
        try:
            threshold = float(sys.argv[3])
        except ValueError:
            print("Error: Threshold must be a numeric value.")
            sys.exit(1)

    print(f"Using input file: {input_file}")
    print(f"Using output file: {output_file}")
    print(f"Filtering customers with purchases > {threshold}")

    # Execution pipeline
    data = load_json(input_file)
    filtered_data = filter_customers(data, threshold)
    save_to_csv(filtered_data, output_file)

if __name__ == "__main__":
    main()

