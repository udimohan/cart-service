"""Tests for catalog_00308."""

import pytest

from cartservice.generated.catalog_00308 import (
    Product_00308,
    bucket_by_tag_00308,
    is_valid_sku_00308,
    price_with_tax_00308,
)


def test_price_with_tax_00308():
    assert price_with_tax_00308(1000, 500) == 1050


def test_price_with_tax_negative_00308():
    with pytest.raises(ValueError):
        price_with_tax_00308(1000, -1)


def test_is_valid_sku_00308():
    assert is_valid_sku_00308("abc123")
    assert not is_valid_sku_00308("")


def test_bucket_by_tag_00308():
    p = Product_00308("s1", 100, ["a"])
    assert bucket_by_tag_00308([p]) == {"a": ["s1"]}
