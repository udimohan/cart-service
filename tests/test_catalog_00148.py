"""Tests for catalog_00148."""

import pytest

from cartservice.generated.catalog_00148 import (
    Product_00148,
    bucket_by_tag_00148,
    is_valid_sku_00148,
    price_with_tax_00148,
)


def test_price_with_tax_00148():
    assert price_with_tax_00148(1000, 500) == 1050


def test_price_with_tax_negative_00148():
    with pytest.raises(ValueError):
        price_with_tax_00148(1000, -1)


def test_is_valid_sku_00148():
    assert is_valid_sku_00148("abc123")
    assert not is_valid_sku_00148("")


def test_bucket_by_tag_00148():
    p = Product_00148("s1", 100, ["a"])
    assert bucket_by_tag_00148([p]) == {"a": ["s1"]}
