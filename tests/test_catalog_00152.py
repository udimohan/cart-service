"""Tests for catalog_00152."""

import pytest

from cartservice.generated.catalog_00152 import (
    Product_00152,
    bucket_by_tag_00152,
    is_valid_sku_00152,
    price_with_tax_00152,
)


def test_price_with_tax_00152():
    assert price_with_tax_00152(1000, 500) == 1050


def test_price_with_tax_negative_00152():
    with pytest.raises(ValueError):
        price_with_tax_00152(1000, -1)


def test_is_valid_sku_00152():
    assert is_valid_sku_00152("abc123")
    assert not is_valid_sku_00152("")


def test_bucket_by_tag_00152():
    p = Product_00152("s1", 100, ["a"])
    assert bucket_by_tag_00152([p]) == {"a": ["s1"]}
