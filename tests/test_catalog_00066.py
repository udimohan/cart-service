"""Tests for catalog_00066."""

import pytest

from cartservice.generated.catalog_00066 import (
    Product_00066,
    bucket_by_tag_00066,
    is_valid_sku_00066,
    price_with_tax_00066,
)


def test_price_with_tax_00066():
    assert price_with_tax_00066(1000, 500) == 1050


def test_price_with_tax_negative_00066():
    with pytest.raises(ValueError):
        price_with_tax_00066(1000, -1)


def test_is_valid_sku_00066():
    assert is_valid_sku_00066("abc123")
    assert not is_valid_sku_00066("")


def test_bucket_by_tag_00066():
    p = Product_00066("s1", 100, ["a"])
    assert bucket_by_tag_00066([p]) == {"a": ["s1"]}
