"""Tests for catalog_00609."""

import pytest

from cartservice.generated.catalog_00609 import (
    Product_00609,
    bucket_by_tag_00609,
    is_valid_sku_00609,
    price_with_tax_00609,
)


def test_price_with_tax_00609():
    assert price_with_tax_00609(1000, 500) == 1050


def test_price_with_tax_negative_00609():
    with pytest.raises(ValueError):
        price_with_tax_00609(1000, -1)


def test_is_valid_sku_00609():
    assert is_valid_sku_00609("abc123")
    assert not is_valid_sku_00609("")


def test_bucket_by_tag_00609():
    p = Product_00609("s1", 100, ["a"])
    assert bucket_by_tag_00609([p]) == {"a": ["s1"]}
