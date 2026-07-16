"""Tests for catalog_00402."""

import pytest

from cartservice.generated.catalog_00402 import (
    Product_00402,
    bucket_by_tag_00402,
    is_valid_sku_00402,
    price_with_tax_00402,
)


def test_price_with_tax_00402():
    assert price_with_tax_00402(1000, 500) == 1050


def test_price_with_tax_negative_00402():
    with pytest.raises(ValueError):
        price_with_tax_00402(1000, -1)


def test_is_valid_sku_00402():
    assert is_valid_sku_00402("abc123")
    assert not is_valid_sku_00402("")


def test_bucket_by_tag_00402():
    p = Product_00402("s1", 100, ["a"])
    assert bucket_by_tag_00402([p]) == {"a": ["s1"]}
