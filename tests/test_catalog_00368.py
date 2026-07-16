"""Tests for catalog_00368."""

import pytest

from cartservice.generated.catalog_00368 import (
    Product_00368,
    bucket_by_tag_00368,
    is_valid_sku_00368,
    price_with_tax_00368,
)


def test_price_with_tax_00368():
    assert price_with_tax_00368(1000, 500) == 1050


def test_price_with_tax_negative_00368():
    with pytest.raises(ValueError):
        price_with_tax_00368(1000, -1)


def test_is_valid_sku_00368():
    assert is_valid_sku_00368("abc123")
    assert not is_valid_sku_00368("")


def test_bucket_by_tag_00368():
    p = Product_00368("s1", 100, ["a"])
    assert bucket_by_tag_00368([p]) == {"a": ["s1"]}
