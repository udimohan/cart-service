"""Tests for catalog_00331."""

import pytest

from cartservice.generated.catalog_00331 import (
    Product_00331,
    bucket_by_tag_00331,
    is_valid_sku_00331,
    price_with_tax_00331,
)


def test_price_with_tax_00331():
    assert price_with_tax_00331(1000, 500) == 1050


def test_price_with_tax_negative_00331():
    with pytest.raises(ValueError):
        price_with_tax_00331(1000, -1)


def test_is_valid_sku_00331():
    assert is_valid_sku_00331("abc123")
    assert not is_valid_sku_00331("")


def test_bucket_by_tag_00331():
    p = Product_00331("s1", 100, ["a"])
    assert bucket_by_tag_00331([p]) == {"a": ["s1"]}
