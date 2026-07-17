"""Tests for catalog_00639."""

import pytest

from cartservice.generated.catalog_00639 import (
    Product_00639,
    bucket_by_tag_00639,
    is_valid_sku_00639,
    price_with_tax_00639,
)


def test_price_with_tax_00639():
    assert price_with_tax_00639(1000, 500) == 1050


def test_price_with_tax_negative_00639():
    with pytest.raises(ValueError):
        price_with_tax_00639(1000, -1)


def test_is_valid_sku_00639():
    assert is_valid_sku_00639("abc123")
    assert not is_valid_sku_00639("")


def test_bucket_by_tag_00639():
    p = Product_00639("s1", 100, ["a"])
    assert bucket_by_tag_00639([p]) == {"a": ["s1"]}
