"""Tests for catalog_01266."""

import pytest

from cartservice.generated.catalog_01266 import (
    Product_01266,
    bucket_by_tag_01266,
    is_valid_sku_01266,
    price_with_tax_01266,
)


def test_price_with_tax_01266():
    assert price_with_tax_01266(1000, 500) == 1050


def test_price_with_tax_negative_01266():
    with pytest.raises(ValueError):
        price_with_tax_01266(1000, -1)


def test_is_valid_sku_01266():
    assert is_valid_sku_01266("abc123")
    assert not is_valid_sku_01266("")


def test_bucket_by_tag_01266():
    p = Product_01266("s1", 100, ["a"])
    assert bucket_by_tag_01266([p]) == {"a": ["s1"]}
