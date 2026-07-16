"""Tests for catalog_00708."""

import pytest

from cartservice.generated.catalog_00708 import (
    Product_00708,
    bucket_by_tag_00708,
    is_valid_sku_00708,
    price_with_tax_00708,
)


def test_price_with_tax_00708():
    assert price_with_tax_00708(1000, 500) == 1050


def test_price_with_tax_negative_00708():
    with pytest.raises(ValueError):
        price_with_tax_00708(1000, -1)


def test_is_valid_sku_00708():
    assert is_valid_sku_00708("abc123")
    assert not is_valid_sku_00708("")


def test_bucket_by_tag_00708():
    p = Product_00708("s1", 100, ["a"])
    assert bucket_by_tag_00708([p]) == {"a": ["s1"]}
