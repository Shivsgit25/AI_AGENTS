from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """
        Add Two numbers
    """
    return a+b


@mcp.tool()
def multiply(a:int,b:int)->int:
    """ Multiply two number """

    return a*b

# we will use Transport = stdio standard input output it tells the server to receive and respond to a call in this std way

if __name__ == "__main__":
    mcp.run(transport="stdio")