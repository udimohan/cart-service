"""Tests for catalog_00845."""

import pytest

from cartservice.generated.catalog_00845 import (
    Product_00845,
    bucket_by_tag_00845,
    is_valid_sku_00845,
    price_with_tax_00845,
)


def test_price_with_tax_00845():
    assert price_with_tax_00845(1000, 500) == 1050


def test_price_with_tax_negative_00845():
    with pytest.raises(ValueError):
        price_with_tax_00845(1000, -1)


def test_is_valid_sku_00845():
    assert is_valid_sku_00845("abc123")
    assert not is_valid_sku_00845("")


def test_bucket_by_tag_00845():
    p = Product_00845("s1", 100, ["a"])
    assert bucket_by_tag_00845([p]) == {"a": ["s1"]}
