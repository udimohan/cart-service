"""Tests for catalog_00466."""

import pytest

from cartservice.generated.catalog_00466 import (
    Product_00466,
    bucket_by_tag_00466,
    is_valid_sku_00466,
    price_with_tax_00466,
)


def test_price_with_tax_00466():
    assert price_with_tax_00466(1000, 500) == 1050


def test_price_with_tax_negative_00466():
    with pytest.raises(ValueError):
        price_with_tax_00466(1000, -1)


def test_is_valid_sku_00466():
    assert is_valid_sku_00466("abc123")
    assert not is_valid_sku_00466("")


def test_bucket_by_tag_00466():
    p = Product_00466("s1", 100, ["a"])
    assert bucket_by_tag_00466([p]) == {"a": ["s1"]}
