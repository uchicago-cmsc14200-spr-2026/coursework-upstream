import os
import pytest
import re
import textwrap
from typing import Callable

from task1 import compose, fixpoint, apply_pipeline, reify_pipeline
from task2 import concat_map
from task3 import Tree, TreeNode
from task5 import TUI
import task2
import task4


## TASK 1


double = lambda n: n * 2
square = lambda n: n**2
double_and_square = compose(square, double)
square_and_double = compose(double, square)


def test_task1_compose_square_double_range7() -> None:
    actual = list(enumerate(map(double_and_square, range(7))))
    expected = [(0, 0), (1, 4), (2, 16), (3, 36), (4, 64), (5, 100), (6, 144)]
    assert actual == expected


def test_task1_compose_double_square_range7() -> None:
    actual = list(enumerate(map(square_and_double, range(7))))
    expected = [(0, 0), (1, 2), (2, 8), (3, 18), (4, 32), (5, 50), (6, 72)]
    assert actual == expected


def test_task1_fixpoint_div2_256() -> None:
    actual = fixpoint(lambda n: n // 2, 256)
    expected = [256, 128, 64, 32, 16, 8, 4, 2, 1, 0]
    assert actual == expected


def test_task1_fixpoint_div2_142() -> None:
    actual = fixpoint(lambda n: n // 2, 142)
    expected = [142, 71, 35, 17, 8, 4, 2, 1, 0]
    assert actual == expected


def test_task1_apply_pipeline_sss_3() -> None:
    assert apply_pipeline([square, square, square], 3) == 6561


def test_task1_apply_pipeline_dsds_3() -> None:
    assert apply_pipeline([double, square, double, square], 3) == 5184


def test_task1_apply_pipeline_sdsd_3() -> None:
    assert apply_pipeline([square, double, square, double], 3) == 648


def test_task1_reify_pipeline_sss_3() -> None:
    sss = reify_pipeline([square, square, square])
    assert sss(3) == 6561


def test_task1_reify_pipeline_dsds_3() -> None:
    dsds = reify_pipeline([double, square, double, square])
    assert dsds(3) == 5184


def test_task1_reify_pipeline_sdsd_3() -> None:
    sdsd = reify_pipeline([square, double, square, double])
    assert sdsd(3) == 648


## Added for Phase 2


def test_task1_fixpoint_const_3_3() -> None:
    const3 = lambda n: 3
    assert fixpoint(const3, 3) == [3]


def test_task1_fixpoint_const_3_1() -> None:
    const3 = lambda n: 3
    assert fixpoint(const3, 1) == [1, 3]


def test_task1_apply_pipeline_empty_3() -> None:
    assert apply_pipeline([], 3) == 3


def test_task1_reify_pipeline_empty() -> None:
    f = reify_pipeline([])
    for i in range(10, 142):
        assert f(i) == i


## TASK 2


def test_task2_concat_map_repeat_range6() -> None:
    actual = concat_map(lambda n: [n] * n, list(range(6)))
    expected = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    assert actual == expected


def test_task2_concat_map_const_empty_range6() -> None:
    actual = concat_map(lambda n: [], list(range(6)))
    assert actual == []


def test_task2_concat_map_keep_even_range6() -> None:
    actual = concat_map(lambda n: [n] if n % 2 == 0 else [], list(range(6)))
    assert actual == [0, 2, 4]


def test_task2_my_map_square_empty() -> None:
    assert task2.my_map(square, []) == []


def test_task2_my_map_square_range6() -> None:
    assert task2.my_map(square, list(range(6))) == [0, 1, 4, 9, 16, 25]


def test_task2_my_filter_even_empty() -> None:
    assert task2.my_filter(lambda n: n % 2 == 0, []) == []


def test_task2_my_filter_even_range6() -> None:
    assert task2.my_filter(lambda n: n % 2 == 0, list(range(6))) == [0, 2, 4]


## TASK 3


t1 = TreeNode(1)
t3 = TreeNode(1, [TreeNode(2), TreeNode(3)])
t4 = TreeNode(1, [TreeNode(2, [TreeNode(3, [TreeNode(4, [])])])])


## Added for Phase 2
def linked_list(n: int) -> Tree:
    tree = TreeNode(n)
    for i in range(n - 1, 0, -1):
        tree = TreeNode(i, [tree])
    return tree


ll8 = linked_list(8)


## Added for Phase 2
def weird_tree(max_level: int) -> Tree:

    def trees_at_level(level: int) -> list[Tree]:
        if level > max_level:
            return []
        else:
            return [
                TreeNode(level, trees_at_level(level + 1)) for _ in range(level)
            ]

    trees_at_level_1 = trees_at_level(1)
    assert len(trees_at_level_1) == 1
    return trees_at_level_1[0]


wt3 = weird_tree(3)


@pytest.mark.parametrize(
    "tree,expected",
    [
        (t1, "(L 2)"),
        (t3, "(T 2 [(L 4) (L 6)])"),
        (t4, "(T 2 [(T 4 [(T 6 [(L 8)])])])"),
        (
            ll8,
            "(T 2 [(T 4 [(T 6 [(T 8 [(T 10 [(T 12 [(T 14 [(L 16)])])])])])])])",
        ),
        (wt3, "(T 2 [(T 4 [(L 6) (L 6) (L 6)]) (T 4 [(L 6) (L 6) (L 6)])])"),
    ],
)
def test_task3_map_examples(tree: Tree, expected: str) -> None:
    assert str(tree.map(lambda n: n * 2)) == expected


@pytest.mark.parametrize(
    "tree,expected", [(t1, 1), (t3, 6), (t4, 10), (ll8, 36), (wt3, 23)]
)
def test_task3_reduce_examples(tree: Tree, expected: str) -> None:
    assert tree.reduce(lambda res, n: res + n, 0) == expected


@pytest.mark.parametrize(
    "tree,expected", [(t1, 1), (t3, 6), (t4, 10), (ll8, 36), (wt3, 23)]
)
def test_task3_sum_examples(tree: Tree, expected: str) -> None:
    assert tree.sum() == expected


@pytest.mark.parametrize(
    "tree,expected", [(t1, 1), (t3, 3), (t4, 4), (ll8, 8), (wt3, 9)]
)
def test_task3_size_examples(tree: Tree, expected: str) -> None:
    assert tree.size() == expected


@pytest.mark.parametrize(
    "tree,expected", [(t1, 1), (t3, 1), (t4, 1), (ll8, 1), (wt3, 1)]
)
def test_task3_min_examples(tree: Tree, expected: str) -> None:
    assert tree.min() == expected


@pytest.mark.parametrize(
    "tree,expected", [(t1, 1), (t3, 3), (t4, 4), (ll8, 8), (wt3, 3)]
)
def test_task3_max_examples(tree: Tree, expected: str) -> None:
    assert tree.max() == expected


## TASK 4


def make_fib_m() -> Callable[[int], int]:
    @task4.memoize
    def fib(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return fib


def make_fib_t() -> Callable[[int], int]:
    @task4.trace
    def fib(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return fib


def make_fib_tm() -> Callable[[int], int]:
    @task4.trace
    @task4.memoize
    def fib(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return fib


def test_task4_fib_m_5() -> None:
    fib = make_fib_m()
    assert fib(5) == 5


def test_task4_fib_m_100() -> None:
    fib = make_fib_m()
    assert fib(100) == 354224848179261915075


# https://docs.pytest.org/en/6.2.x/capture.html


def test_task4_fib_t_0(capsys: pytest.CaptureFixture[str]) -> None:
    fib = make_fib_t()
    fib(0)
    actual = capsys.readouterr().out
    expected = """
        / fib(0)
        \\ 0
    """
    assert actual.strip() == textwrap.dedent(expected).strip()


def test_task4_fib_t_2(capsys: pytest.CaptureFixture[str]) -> None:
    fib = make_fib_t()
    fib(2)
    actual = capsys.readouterr().out
    expected = """
        / fib(2)
        | / fib(1)
        | \\ 1
        | / fib(0)
        | \\ 0
        \\ 1
    """
    assert actual.strip() == textwrap.dedent(expected).strip()


def test_task4_fib_t_5(capsys: pytest.CaptureFixture[str]) -> None:
    fib = make_fib_t()
    fib(5)
    actual = capsys.readouterr().out
    expected = """
        / fib(5)
        | / fib(4)
        | | / fib(3)
        | | | / fib(2)
        | | | | / fib(1)
        | | | | \\ 1
        | | | | / fib(0)
        | | | | \\ 0
        | | | \\ 1
        | | | / fib(1)
        | | | \\ 1
        | | \\ 2
        | | / fib(2)
        | | | / fib(1)
        | | | \\ 1
        | | | / fib(0)
        | | | \\ 0
        | | \\ 1
        | \\ 3
        | / fib(3)
        | | / fib(2)
        | | | / fib(1)
        | | | \\ 1
        | | | / fib(0)
        | | | \\ 0
        | | \\ 1
        | | / fib(1)
        | | \\ 1
        | \\ 2
        \\ 5
    """
    assert actual.strip() == textwrap.dedent(expected).strip()


def test_task4_fib_tm(capsys: pytest.CaptureFixture[str]) -> None:
    fib = make_fib_tm()
    fib(5)
    actual = capsys.readouterr().out
    expected = """
        / fib(5)
        | / fib(4)
        | | / fib(3)
        | | | / fib(2)
        | | | | / fib(1)
        | | | | \\ 1
        | | | | / fib(0)
        | | | | \\ 0
        | | | \\ 1
        | | | / fib(1)
        | | | \\ 1
        | | \\ 2
        | | / fib(2)
        | | \\ 1
        | \\ 3
        | / fib(3)
        | \\ 2
        \\ 5
    """
    assert actual.strip() == textwrap.dedent(expected).strip()


## Added for Phase 2


def make_fact_m() -> Callable[[int], int]:
    @task4.memoize
    def fact(n: int) -> int:
        if n <= 0:
            return 1
        else:
            return n * fact(n - 1)

    return fact


def make_even_odd_t() -> tuple[Callable[[int], int], Callable[[int], int]]:
    @task4.trace
    def even(n: int) -> int:
        if n == 0:
            return 1
        else:
            return odd(n - 1)

    @task4.trace
    def odd(n: int) -> int:
        if n == 0:
            return 0
        else:
            return even(n - 1)

    return (even, odd)


def test_task4_fib_and_fact_m_T1() -> None:
    fib = make_fib_m()
    fact = make_fact_m()
    assert fact(5) == 120
    assert fib(5) == 5
    assert fact(5) == 120


def test_task4_fib_and_fact_m_T2() -> None:
    fib = make_fib_m()
    fact = make_fact_m()
    assert fact(14) == 87178291200
    assert fib(100) == 354224848179261915075
    assert fact(14) == 87178291200


def test_task4_even_t_10(capsys: pytest.CaptureFixture[str]) -> None:
    even, odd = make_even_odd_t()
    even(10)
    actual = capsys.readouterr().out
    expected = """
        / even(10)
        / odd(9)
        | / even(8)
        | / odd(7)
        | | / even(6)
        | | / odd(5)
        | | | / even(4)
        | | | / odd(3)
        | | | | / even(2)
        | | | | / odd(1)
        | | | | | / even(0)
        | | | | | \\ 1
        | | | | \\ 1
        | | | | \\ 1
        | | | \\ 1
        | | | \\ 1
        | | \\ 1
        | | \\ 1
        | \\ 1
        | \\ 1
        \\ 1
        \\ 1
    """
    assert actual.strip() == textwrap.dedent(expected).strip()


## TASK 5


@pytest.mark.parametrize(
    "s,expected",
    [
        ("123", 123),
        ("", None),
        ("?!?!?", None),
        ("123.123", None),
        ("-3.14", None),
        ("-3", -3),
        ("142", 142),
        ("14200", 14200),
        ("11111", 11111),
        ("Can I offer you some food for thought? 🍎🍌🤔💭", None),
        ("ugh, this is boring", None),
    ],
)
def test_task5_read_optional_int(s: str, expected: int | None) -> None:
    assert TUI.read_optional_int(s) == expected


## Added for Phase 2


@pytest.mark.parametrize(
    "s,expected",
    [
        ("0", 0),
        ("-0", 0),
        ("-", None),
        ("1 4 2", None),
        ("142OO", None),
        ('"142OO"', None),
    ],
)
def test_task5_read_optional_int_more(s: str, expected: int | None) -> None:
    assert TUI.read_optional_int(s) == expected


@pytest.mark.parametrize(
    "in_script,responses",
    [
        (
            "tests/001.in",  # Test with a "0", "-0", "o", "O"
            [
                "Let's have a chat about numbers!",
                "Yes, 0 is a nice number.",
                "Yes, 0 is a nice number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Okay, goodbye.",
            ],
        ),
        (
            "tests/002.in",  # Test with '"123"', "'123'", '"one"', "'two'",
            [
                "Let's have a chat about numbers!",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Okay, goodbye.",
            ],
        ),
        (
            "tests/003.in",  # Test with " ", " 123", "123 ", "1 2 3"
            [
                "Let's have a chat about numbers!",
                "Hmm, that doesn't seem like a number.",
                "Yes, 123 is a nice number.",
                "Yes, 123 is a nice number.",
                "Hmm, that doesn't seem like a number.",
                "Okay, goodbye.",
            ],
        ),
        (
            "tests/004.in",  # Test with "142", "14200"
            [
                "Let's have a chat about numbers!",
                "Indeed! That _is_ a nice number!",
                "Indeed! That _is_ a nice number!",
                "Okay, goodbye.",
            ],
        ),
        (
            "tests/005.in",  # Test with "-142.0", "-14200.0", "142.0", "14200.0", "798.24", "-12.33"
            [
                "Let's have a chat about numbers!",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Hmm, that doesn't seem like a number.",
                "Okay, goodbye.",
            ],
        ),
    ],
)
def test_task5_io(in_script: str, responses: list[str]) -> None:
    os.system(f"cat {in_script} | python3 task5.py > temp.out")

    with open("temp.out", "r") as f:
        lines = iter(f.readlines())

    for response in responses:
        line = next(lines)
        while line.strip() == "":
            line = next(lines)

        line_norm = re.sub(r"[^a-z]", "", line.lower())
        response_norm = re.sub(r"[^a-z]", "", response.lower())

        assert response_norm in line_norm, (response, line)

    os.system("rm temp.out")
