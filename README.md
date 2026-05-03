# unit-convertor-mcp

A minimal MCP server for metric unit conversion. Converts temperatures between Celsius and Fahrenheit.

## Installation

### Prerequisites

- Python 3.14 or higher
- `uv` package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd unit-convertor-mcp
```

2. Install dependencies using `uv`:

```bash
uv sync
```

## Running with fastMCP

### Start the MCP Server

Run the server using `uv` with fastMCP:

```bash
uv run fastmcp run temperature_converter.py:mcp --transport http --port 8000
```

This will start the MCP server on `http://localhost:8000`.

**Options:**

- `--transport http` - Use HTTP transport (default)
- `--port 8000` - Run on port 8000 (you can change this to any available port)

### Alternative: Run directly with Python

```bash
uv run python temperature_converter.py
```

## How to Use

### Tool: `temperature_converter`

Convert temperatures between Celsius and Fahrenheit.

**Parameters:**

- `value` (float): The temperature value to convert
- `unit` (str): The unit of the input temperature - `"celsius"` or `"fahrenheit"`
- `fraction` (int, optional): Number of decimal places to round to (default: 2)

**Examples:**

Convert 0°C to Fahrenheit:

```python
temperature_converter(value=0, unit="celsius")
# Returns: 32.0
```

Convert 98.6°F to Celsius:

```python
temperature_converter(value=98.6, unit="fahrenheit")
# Returns: 37.0
```

Convert with custom decimal precision:

```python
temperature_converter(value=25, unit="celsius", fraction=4)
# Returns: 77.0
```

### Adding to VSCode

To integrate this MCP server with VSCode Copilot:

1. **Install the MCP Server locally:**

   ```bash
   cd /path/to/unit-convertor-mcp
   uv sync
   ```

2. **Configure VSCode settings:**
   - Open VSCode settings: `Cmd + ,` (macOS) or `Ctrl + ,` (Windows/Linux)
   - Search for "MCP" or open your `settings.json`
   - Add the server configuration:

   ```json
   "copilot.advanced.mcp.servers": {
       "temperature-converter": {
           "command": "uv",
           "args": [
               "run",
               "fastmcp",
               "run",
               "/path/to/unit-convertor-mcp/temperature_converter.py:mcp"
           ]
       }
   }
   ```

3. **Restart VSCode** for the changes to take effect.

4. **Use in Copilot Chat:**
   - Open Copilot Chat (`Cmd + Shift + I` on macOS)
   - Use the `temperature_converter` tool when asking Copilot to convert temperatures
   - Example: "Convert 32 fahrenheit to celsius"
