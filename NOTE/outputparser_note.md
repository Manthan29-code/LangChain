Here’s a list of the **main types of Output Parsers** with a short intro for each:

* * *

### 🔹 Common Output Parsers in LangChain

1. **`StrOutputParser`**

    - Simplest parser.
    - Returns the raw string output from the LLM.
    - Use when you don’t need structured data.
2. **`RegexParser`**

    - Uses **regular expressions** to extract specific parts of the LLM output.
    - Helpful if you expect outputs in a known textual pattern.
3. **`PydanticOutputParser`**

    - Parses output into a **Pydantic model** (Python dataclass-like structure).
    - Ensures data validation & type safety.
    - Great for strict structured outputs.
4. **`CommaSeparatedListOutputParser`**

    - Converts the output into a **list of strings** by splitting with commas.
    - Example: `"apple, banana, mango"` → `["apple", "banana", "mango"]`.
5. **`DatetimeOutputParser`**

    - Extracts **dates and times** from model output and returns them as `datetime` objects.
    - Useful for scheduling or calendar-based apps.
6. **`BooleanOutputParser`**

    - Converts model output to a **boolean (`True`/`False`)**.
    - Example: Output `"yes"` → `True`.
7. **`StructuredOutputParser`**

    - Lets you define an **expected schema** (via JSON Schema).
    - LLM output is parsed & validated against the schema.
    - Good for API-like structured responses.
8. **`JsonOutputParser`**

    - Ensures LLM output is valid **JSON**.
    - Automatically parses JSON into a Python dict.
9. **`XMLOutputParser`**

    - Parses XML-based outputs into structured data.
    - Rarely used, but useful if your LLM prompt enforces XML tags.
10. **`RetryOutputParser`**

    - Wraps another parser.
    - If parsing fails, it automatically asks the LLM again to reformat properly.

* * *

👉 In practice:

- Use `StrOutputParser` if you just need plain text.
- Use `JsonOutputParser` / `StructuredOutputParser` if you need structured data for APIs.
- Use `PydanticOutputParser` if you want Python type-safety and validation.