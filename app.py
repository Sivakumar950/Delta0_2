import threading
import time
from typing import List, Callable, Any

# Step 1: Create a decorator to time function execution
def timer(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Step 2: Define a class with multiple methods to manipulate "Hello, World!"
class HelloWorldManipulator:
    def __init__(self, message: str):
        self.message = message

    @timer
    def reverse_message(self) -> str:
        return self.message[::-1]

    @timer
    def to_uppercase(self) -> str:
        return self.message.upper()

    @timer
    def char_count(self) -> int:
        return len(self.message)

    @timer
    def split_message(self) -> List[str]:
        return self.message.split()

    @timer
    def fancy_display(self) -> None:
        for char in self.message:
            print(char, end=" ")
            time.sleep(0.1)  # Adds delay to simulate typing effect
        print()

# Step 3: Utilize threading to run multiple operations
def run_in_thread(func: Callable, *args: Any) -> threading.Thread:
    thread = threading.Thread(target=func, args=args)
    thread.start()
    return thread

# Step 4: Main function to initiate complex operations
@timer
def main() -> None:
    manipulator = HelloWorldManipulator("Hello, World!")

    # Display original message
    print("Original Message:", manipulator.message)

    # Run various transformations in threads
    threads = [
        run_in_thread(print, "Reversed:", manipulator.reverse_message()),
        run_in_thread(print, "Uppercase:", manipulator.to_uppercase()),
        run_in_thread(print, "Character Count:", manipulator.char_count()),
        run_in_thread(print, "Split Message:", manipulator.split_message())
    ]

    # Fancy display is not threaded to ensure readability
    manipulator.fancy_display()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Execute the program
if __name__ == "__main__":
    main()
