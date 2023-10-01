import matplotlib.pyplot as plt
from io import BytesIO


def main(context):
    if context.req.method == "GET":
        context.log(context.req.body)

        x_axis = [1, 2, 3]
        y_axis = ["A", "B", "C"]
        plt.plot(x_axis, y_axis)

        plt.xlabel('num')
        plt.ylabel('let')

        buf = BytesIO()
        plt.savefig(buf, format="png")
        return context.res.send(buf.getvalue())

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # # The `ctx.req` object contains the request data
    # if context.req.method == "GET":
    #     # Send a response with the res object helpers
    #     # `ctx.res.send()` dispatches a string back to the client
    #     return context.res.send(buf.getvalue())

    # `ctx.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build Fast. Scale Big. All in One Place.",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )


# if __name__ == "__main__":
#     main(None)
#     pass
