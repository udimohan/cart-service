"""Tests for catalog_00508."""

import pytest

from cartservice.generated.catalog_00508 import (
    Product_00508,
    bucket_by_tag_00508,
    is_valid_sku_00508,
    price_with_tax_00508,
)


def test_price_with_tax_00508():
    assert price_with_tax_00508(1000, 500) == 1050


def test_price_with_tax_negative_00508():
    with pytest.raises(ValueError):
        price_with_tax_00508(1000, -1)


def test_is_valid_sku_00508():
    assert is_valid_sku_00508("abc123")
    assert not is_valid_sku_00508("")


def test_bucket_by_tag_00508():
    p = Product_00508("s1", 100, ["a"])
    assert bucket_by_tag_00508([p]) == {"a": ["s1"]}
