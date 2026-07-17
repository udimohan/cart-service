"""Tests for catalog_00828."""

import pytest

from cartservice.generated.catalog_00828 import (
    Product_00828,
    bucket_by_tag_00828,
    is_valid_sku_00828,
    price_with_tax_00828,
)


def test_price_with_tax_00828():
    assert price_with_tax_00828(1000, 500) == 1050


def test_price_with_tax_negative_00828():
    with pytest.raises(ValueError):
        price_with_tax_00828(1000, -1)


def test_is_valid_sku_00828():
    assert is_valid_sku_00828("abc123")
    assert not is_valid_sku_00828("")


def test_bucket_by_tag_00828():
    p = Product_00828("s1", 100, ["a"])
    assert bucket_by_tag_00828([p]) == {"a": ["s1"]}
