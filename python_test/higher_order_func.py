from typing import Callable


def compute(*args, **kwargs):
    """Performs an operation ('add', 'max', 'min') on the given arguments."""
    if kwargs["operation"] == "add":
        return sum(args)
    elif kwargs["operation"] == "max":
        return max(args)
    elif kwargs["operation"] == "min":
        return min(args)
    else:
        return -1


def partial(func: Callable, *args, **kwargs) -> Callable:
    """Returns a new function with pre-applied arguments and keyword arguments."""

    def wrapper(*new_args, **new_kwargs):
        """Combines previously applied arguments with new ones and calls func."""
        combined_args = args + new_args
        combined_kwargs = {**kwargs, **new_kwargs}
        return func(*combined_args, **combined_kwargs)

    return wrapper


n = int(input().strip())

operation_in = input()

# Step 1: Create a partially applied function
result = partial(compute, operation=operation_in)

# Step 2: Further apply arguments iteratively
for _ in range(n - 1):
    arguments = list(map(int, input().rstrip().split()))
    result = partial(result, *arguments)

# Step 3: Final arguments and function execution
arguments = list(map(int, input().rstrip().split()))

print(str(result(*arguments)) + "\n")
