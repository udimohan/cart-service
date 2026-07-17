"""Tests for catalog_00051."""

import pytest

from cartservice.generated.catalog_00051 import (
    Product_00051,
    bucket_by_tag_00051,
    is_valid_sku_00051,
    price_with_tax_00051,
)


def test_price_with_tax_00051():
    assert price_with_tax_00051(1000, 500) == 1050


def test_price_with_tax_negative_00051():
    with pytest.raises(ValueError):
        price_with_tax_00051(1000, -1)


def test_is_valid_sku_00051():
    assert is_valid_sku_00051("abc123")
    assert not is_valid_sku_00051("")


def test_bucket_by_tag_00051():
    p = Product_00051("s1", 100, ["a"])
    assert bucket_by_tag_00051([p]) == {"a": ["s1"]}
