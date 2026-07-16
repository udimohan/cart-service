"""Tests for catalog_00779."""

import pytest

from cartservice.generated.catalog_00779 import (
    Product_00779,
    bucket_by_tag_00779,
    is_valid_sku_00779,
    price_with_tax_00779,
)


def test_price_with_tax_00779():
    assert price_with_tax_00779(1000, 500) == 1050


def test_price_with_tax_negative_00779():
    with pytest.raises(ValueError):
        price_with_tax_00779(1000, -1)


def test_is_valid_sku_00779():
    assert is_valid_sku_00779("abc123")
    assert not is_valid_sku_00779("")


def test_bucket_by_tag_00779():
    p = Product_00779("s1", 100, ["a"])
    assert bucket_by_tag_00779([p]) == {"a": ["s1"]}
