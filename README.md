# Python Libraries Implemented in C

## Introduction
For this project, I explored how Python can use libraries and functions written in C to improve performance. I wanted to understand why languages like C can perform certain operations much faster than Python, even when doing the exact same calculations.

## What I Explored
I looked at how Python and C store data differently and how those differences affect performance.

Some of the things I explored included:

- **Memory Management:** How C stores array values directly in memory compared to Python lists, which store references to integer objects.
- **Cost of Addition:** Why adding values in a Python loop involves more overhead than adding values in a C loop.
- **Python and C Integration:** How to compile a C function into a shared library (`.so` file) and call it from Python using `ctypes`.
- **NumPy:** How NumPy provides C-style arrays that allow calculations to run efficiently using optimized low-level code.

## My Experiments
I created functions in Python, NumPy, and C to sum 10 million integers. I then measured their execution times to compare their performance.

My results showed that NumPy was approximately 65–80 times faster than a regular Python loop in my tests.

## Most Interesting Discoveries

1. **How Python and C Store Data Differently:** Python lists store references to separate integer objects, while C arrays store values directly in contiguous memory. This creates differences in memory usage and performance.

2. **How Python Can Use C Functions:** I learned that Python can load compiled C libraries and call their functions directly using `ctypes`. This allows Python to use the performance benefits of C without having to write an entire program in C.

3. **How Much Faster NumPy Can Be:** I was surprised by how much faster NumPy was at summing large arrays. Its ability to use optimized low-level code makes it much more efficient than a regular Python loop.

## Conclusion
This project helped me understand that programming language performance depends on more than just the operation being performed. How data is stored, how memory is accessed, and how calculations are executed can make a significant difference. I also learned how Python and C can work together to combine Python's simplicity with C's performance.

## Link to Slides
https://docs.google.com/presentation/d/1GO5F8P4l1YDAAgfgJ636BNK5lKRmX3v2lwLJblwXBFI/edit?usp=sharing

## Additional Resources
https://numpy.org/ /n
https://docs.python.org/3/library/ctypes.html
