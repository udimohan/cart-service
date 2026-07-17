"""Tests for catalog_00487."""

import pytest

from cartservice.generated.catalog_00487 import (
    Product_00487,
    bucket_by_tag_00487,
    is_valid_sku_00487,
    price_with_tax_00487,
)


def test_price_with_tax_00487():
    assert price_with_tax_00487(1000, 500) == 1050


def test_price_with_tax_negative_00487():
    with pytest.raises(ValueError):
        price_with_tax_00487(1000, -1)


def test_is_valid_sku_00487():
    assert is_valid_sku_00487("abc123")
    assert not is_valid_sku_00487("")


def test_bucket_by_tag_00487():
    p = Product_00487("s1", 100, ["a"])
    assert bucket_by_tag_00487([p]) == {"a": ["s1"]}
