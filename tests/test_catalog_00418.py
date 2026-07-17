"""Tests for catalog_00418."""

import pytest

from cartservice.generated.catalog_00418 import (
    Product_00418,
    bucket_by_tag_00418,
    is_valid_sku_00418,
    price_with_tax_00418,
)


def test_price_with_tax_00418():
    assert price_with_tax_00418(1000, 500) == 1050


def test_price_with_tax_negative_00418():
    with pytest.raises(ValueError):
        price_with_tax_00418(1000, -1)


def test_is_valid_sku_00418():
    assert is_valid_sku_00418("abc123")
    assert not is_valid_sku_00418("")


def test_bucket_by_tag_00418():
    p = Product_00418("s1", 100, ["a"])
    assert bucket_by_tag_00418([p]) == {"a": ["s1"]}
