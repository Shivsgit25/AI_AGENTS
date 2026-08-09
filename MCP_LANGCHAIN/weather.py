from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")


@mcp.tool()
async def getWeather(location: str)->str:
    """get the weather of location """
    return "Its Rainy in Mumbai"

# when we use transport="streamable-http" it runs the service as an api itself

if __name__=="__main__":
    mcp.run(transport="streamable-http")