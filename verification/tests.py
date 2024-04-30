"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
    {
        "input": [["Fahrenheit 451", "Ray Bradbury"], ["To Kill a Mockingbird", "Harper Lee"]],
        "answer": {
            "livro1": {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury"},
            "livro2": {"titulo": "To Kill a Mockingbird", "autor": "Harper Lee"}
        }
    },
    {
        "input": [["The Great Gatsby", "F. Scott Fitzgerald"], ["The Catcher in the Rye", "J.D. Salinger"], ["1984", "George Orwell"]],
        "answer": {
            "livro1": {"titulo": "The Great Gatsby", "autor": "F. Scott Fitzgerald"},
            "livro2": {"titulo": "The Catcher in the Rye", "autor": "J.D. Salinger"},
            "livro3": {"titulo": "1984", "autor": "George Orwell"}
        }
    }

    ]
}
