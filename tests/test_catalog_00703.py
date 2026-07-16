"""Tests for catalog_00703."""

import pytest

from cartservice.generated.catalog_00703 import (
    Product_00703,
    bucket_by_tag_00703,
    is_valid_sku_00703,
    price_with_tax_00703,
)


def test_price_with_tax_00703():
    assert price_with_tax_00703(1000, 500) == 1050


def test_price_with_tax_negative_00703():
    with pytest.raises(ValueError):
        price_with_tax_00703(1000, -1)


def test_is_valid_sku_00703():
    assert is_valid_sku_00703("abc123")
    assert not is_valid_sku_00703("")


def test_bucket_by_tag_00703():
    p = Product_00703("s1", 100, ["a"])
    assert bucket_by_tag_00703([p]) == {"a": ["s1"]}
