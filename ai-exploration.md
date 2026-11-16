# AI Learning Reflection: Python Libraries Implemented in C

I initially approached this topic by trying to understand why Python can be slower than languages like C when performing the same calculations. I was particularly interested in how Python libraries like NumPy achieve better performance. As I explored the topic, my questions became more specific. I started looking into how Python and C store data differently, why Python loops have more overhead, and how Python can call functions written in C using a shared library.

A major part of my exploration involved working with AI to write functions that summed 10 million integers using regular Python, NumPy, and C. I used AI to help write the different implementations, set up the performance tests, and figure out how to compile the C code into a shared library that Python could use.

Some representative prompts I used during my exploration were:

1. "Why do Python, NumPy, and C have such different runtimes when summing 10 million integers?"
2. "Why does Python have more overhead when adding values from a list compared to adding values from a C array?"
3. "How can I use ctypes to call a C function from Python, and what commands do I need to compile the C file?"

I used AI as a learning tool throughout the process rather than just asking it to generate my presentation. When I did not understand an explanation, I asked follow-up questions to get a simpler explanation or a more concrete example. I also asked AI to help simplify code and troubleshoot problems when I had trouble installing NumPy and compiling the C library. I then ran the code myself and compared the execution times. This helped me connect the explanations to actual results. One thing I found particularly interesting was that NumPy was around 65–80 times faster than my regular Python loop in my experiment.

If I were to approach this project differently, I would spend more time experimenting with the code before asking AI for explanations. I would also try changing different parts of the implementation to see how they affect performance. Overall, I found that asking follow-up questions, working with AI to develop the code, and testing the results myself was much more useful than simply accepting the first answer AI provided.

# Link to AI Conversation
https://chatgpt.com/share/6afb3760-82a8-83e9-914d-2f69a5150486
