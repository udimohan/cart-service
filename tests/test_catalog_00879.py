"""Tests for catalog_00879."""

import pytest

from cartservice.generated.catalog_00879 import (
    Product_00879,
    bucket_by_tag_00879,
    is_valid_sku_00879,
    price_with_tax_00879,
)


def test_price_with_tax_00879():
    assert price_with_tax_00879(1000, 500) == 1050


def test_price_with_tax_negative_00879():
    with pytest.raises(ValueError):
        price_with_tax_00879(1000, -1)


def test_is_valid_sku_00879():
    assert is_valid_sku_00879("abc123")
    assert not is_valid_sku_00879("")


def test_bucket_by_tag_00879():
    p = Product_00879("s1", 100, ["a"])
    assert bucket_by_tag_00879([p]) == {"a": ["s1"]}
