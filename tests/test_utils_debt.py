import math
import pytest

from src.app.utils.debt_utils import (
    safe_div,
    dispatch_by_key,
    nested_loops,
    normalize_numbers,
    aggregate_stats,
    validate_index,
)

def test_safe_div_ok():
    assert safe_div(10, 2) == 5.0

def test_safe_div_zero():
    with pytest.raises(ValueError):
        safe_div(1, 0)

def test_dispatch_by_key_ok_and_default():
    calls = []
    table = {"a": lambda: (calls.append("a"), "ok-a")[1]}
    assert dispatch_by_key("a", table) == "ok-a"
    assert calls == ["a"]
    assert dispatch_by_key("x", table, default=lambda: "default") == "default"
    with pytest.raises(KeyError):
        dispatch_by_key("x", table)

def test_nested_loops_values():
    assert nested_loops(1) == 1      # 2**1 - 1
    assert nested_loops(4) == 15     # 2**4 - 1
    with pytest.raises(ValueError):
        nested_loops(0)

def test_normalize_numbers_and_errors():
    assert normalize_numbers([0.0, 5.0, 10.0]) == [0.0, 0.5, 1.0]
    with pytest.raises(Exception):
        normalize_numbers([])
    with pytest.raises(Exception):
        normalize_numbers([3.0, 3.0])

def test_aggregate_stats():
    stats = aggregate_stats([1.0, 2.0, 3.0])
    assert stats["min"] == 1.0
    assert stats["max"] == 3.0
    assert stats["mean"] == 2.0
    assert math.isclose(stats["var"], 2.0/3.0, rel_tol=1e-9)

def test_validate_index_ok_and_error():
    seq = ["a", "b", "c"]
    assert validate_index(seq, 1) == "b"
    with pytest.raises(IndexError):
        validate_index(seq, 3)


# ---------- Pruebas opcionales (solo si existen helpers extra) ----------
def _maybe(module_name, attr):
    try:
        mod = __import__(module_name, fromlist=[attr])
        return getattr(mod, attr, None)
    except Exception:
        return None

def test_optional_extras_if_present():
    # Importa helpers opcionales si están disponibles; si no, se salta.
    percentage = _maybe("src.app.utils.debt_utils", "percentage")
    clamp = _maybe("src.app.utils.debt_utils", "clamp")
    chunked = _maybe("src.app.utils.debt_utils", "chunked")
    is_alpha_space = _maybe("src.app.utils.debt_utils", "is_alpha_space")
    validate_length = _maybe("src.app.utils.debt_utils", "validate_length")
    dispatch_with_args = _maybe("src.app.utils.debt_utils", "dispatch_with_args")

    if percentage is not None:
        assert percentage(1, 4) == 25.0
        assert percentage(0, 0) == 0.0

    if clamp is not None:
        assert clamp(10, 0, 5) == 5
        assert clamp(-1, 0, 5) == 0

    if chunked is not None:
        assert list(chunked(range(5), 2)) == [[0, 1], [2, 3], [4]]

    if is_alpha_space is not None:
        assert is_alpha_space("Juan Perez")
        assert not is_alpha_space("Juan Perez 123")

    if validate_length is not None:
        validate_length("hola", min_len=1, max_len=10)

    if dispatch_with_args is not None:
        assert dispatch_with_args("sum", {"sum": lambda x, y: x + y}, 2, 3) == 5