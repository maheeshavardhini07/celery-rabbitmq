from tasks.workers import add, process_data

if __name__ == "__main__":
    print("Sending add task...")
    result = add.delay(10, 20)
    print("Add result:", result.get(timeout=50))

    print("Sending process_data task...")
    result2 = process_data.delay(5)
    print("Process_data result:", result2.get(timeout=10))