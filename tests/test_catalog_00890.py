"""Tests for catalog_00890."""

import pytest

from cartservice.generated.catalog_00890 import (
    Product_00890,
    bucket_by_tag_00890,
    is_valid_sku_00890,
    price_with_tax_00890,
)


def test_price_with_tax_00890():
    assert price_with_tax_00890(1000, 500) == 1050


def test_price_with_tax_negative_00890():
    with pytest.raises(ValueError):
        price_with_tax_00890(1000, -1)


def test_is_valid_sku_00890():
    assert is_valid_sku_00890("abc123")
    assert not is_valid_sku_00890("")


def test_bucket_by_tag_00890():
    p = Product_00890("s1", 100, ["a"])
    assert bucket_by_tag_00890([p]) == {"a": ["s1"]}
