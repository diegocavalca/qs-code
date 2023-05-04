class MathSamples:

    @staticmethod
    def fibonacci(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return MathSamples.fibonacci(n-1) \
                + MathSamples.fibonacci(n-2)