
import odbchelper


def info(object, spacing=10, collapse=1):
    """Print methods and doc string.

    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(
        getattr(object, method))]

    # lambda, a function, avoid to defined inside a function
    # make things neat.
    # it's more appearing in javascript, cause we use them all the time.
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" % (
        method.ljust(spacing),
        processFunc(str(getattr(object, method).__doc__)))
        for method in methodList]))


if __name__ == "__main__":
    # print(info.__doc__)
    info(odbchelper)




#end of file
