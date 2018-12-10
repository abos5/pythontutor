def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.


    Return string."""
    print(params)
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {
        "server": "mpilgrim",
        "database": "master",
        "uid": "sa",
        "pwd": "secret"
    }
    print(buildConnectionString(myParams))
else:
    pass
    # print("printing a __name__ %r" % __name__)
#end of
