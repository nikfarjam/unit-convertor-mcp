from fastmcp import FastMCP

mcp = FastMCP("Temperature Converter MCP Server")

def celsius_to_fahrenheit(celsius, fraction = 2):
    if celsius:
        return round((celsius * 9 / 5 ) + 32, fraction)
    return float('nan')

def fahrenheit_to_celsius(fahrenheit, fraction = 2):
    if fahrenheit:
        return round((fahrenheit - 32) * 5 / 9, fraction)
    return float('nan')

@mcp.tool
def temperature_converter(value: float, unit: str, fraction = 2):
    """
    Convert temperatures between Celsius and Fahrenheit.
    Parameters:
    - value: The temperature value to convert.
    - unit: The unit of the input temperature ('celsius' or 'fahrenheit').
    - fraction: The number of decimal places to round the result to (default is 2).
    Returns:
    - The converted temperature value.
    """
    if unit.lower() == "celsius":
        return celsius_to_fahrenheit(value, fraction)
    elif unit.lower() == "fahrenheit":
        return fahrenheit_to_celsius(value, fraction)
    else:
        raise ValueError("Invalid units. Use 'celsius' or 'fahrenheit'.")

if __name__ == "__main__":
    mcp.run()
