
# Mini Pytest TDD

A tiny exercise to practice **TDD with pytest** using three features:
- `@pytest.mark.parametrize`
- `pytest.raises`
- `pytest.approx`

You'll implement a few simple math functions working purely with basic `float` types, then run the tests and iterate until they pass.

## What you will implement

Open `src/simple_math/core.py` and complete these functions (they currently raise `NotImplementedError`):

- `add(a: float, b: float) -> float`: Return `a + b`.
- `safe_divide(a: float, b: float) -> float`: Return `a / b`; raise `ValueError` if `b == 0.0`.
- `sqrt_approx(x: float, iterations: int = 12) -> float`: Approximate `sqrt(x)` using Newton's method; raise `ValueError` if `x < 0.0`.
- `average(xs: list[float]) -> float`: Return the arithmetic mean; raise `ValueError` for an empty list.

Each function includes a docstring with examples to guide you.

---

## Setup & Run (Poetry only)

1. From the project root, install dependencies:
   ```bash
   poetry install
   ```

2. Run tests:
   ```bash
   poetry run pytest -q
   ```

---

## TDD Workflow Tips

1. **Run tests first** to see failures.
2. Implement the smallest change to make one test pass.
3. Re-run tests, **refactor only after green**.
4. Repeat.

Happy testing! 🎯
